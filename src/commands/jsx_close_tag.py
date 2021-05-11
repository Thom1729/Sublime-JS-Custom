import sublime
import sublime_plugin

TAG_BEGIN_SCOPE = 'meta.tag.js punctuation.definition.tag.begin.js'
TAG_END_SCOPE = 'meta.tag.attributes.js punctuation.definition.tag.end.js'


__all__ = ['JsxCloseTagCommand']


class JsxCloseTagCommand(sublime_plugin.TextCommand):
    def run(self, edit: sublime.Edit, insert_slash: bool = False) -> None:
        for region in reversed(self.view.sel()):  # type: ignore
            pos = region.begin()
            try:
                open_tag = self.find_open_tag(pos)
                text = '%s/%s>' % ('' if insert_slash else '<', open_tag)
                self.view.insert(edit, pos, text)
            except ValueError:
                if insert_slash:
                    self.view.insert(edit, pos, '/')

    def find_open_tag(self, end: int) -> str:
        depth = 0
        while True:
            tag_end = self.find_before(TAG_END_SCOPE, end)

            scope = self.view.scope_name(tag_end)
            target_scope = scope.replace(TAG_END_SCOPE, TAG_BEGIN_SCOPE)

            tag_begin = self.find_before(target_scope, tag_end)
            if self.view.substr(tag_begin) == '/':
                tag_begin = self.find_before(target_scope, tag_begin)

            end = tag_begin

            # Handle self-closing tag
            last_token = self.find_before('- comment', tag_end)
            if self.view.substr(last_token) == '/':
                continue

            # Handle close tag
            first_token = self.find_after('- comment', tag_begin)
            if self.view.substr(first_token) == '/':
                depth += 1
                continue

            # Else, open tag
            if depth == 0:
                if self.view.match_selector(first_token, 'meta.tag.name'):
                    name_end = self.find_after('- meta.tag.name', first_token)
                    name_region = sublime.Region(first_token, name_end)
                    name = self.view.substr(name_region).strip()
                    return name
                else:
                    # Fragment, or invalid
                    return ''
            else:
                depth -= 1
                continue

    def find_before(self, selector: str, pos: int) -> int:
        pos -= 1
        while pos >= 0:
            if self.view.match_selector(pos, selector):
                return pos
            else:
                pos -= 1

        raise ValueError("Can't find open tag.")

    def find_after(self, selector: str, pos: int) -> int:
        pos += 1
        max = self.view.size()
        while pos <= max:
            if self.view.match_selector(pos, selector):
                return pos
            else:
                pos += 1

        raise ValueError("Can't find open tag.")
