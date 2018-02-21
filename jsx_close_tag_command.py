import sublime
import sublime_plugin

TAG_BEGIN_SCOPE = 'punctuation.definition.tag.begin.js'
TAG_END_SCOPE = 'punctuation.definition.tag.end.js'

class JsxCloseTagCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        for region in reversed(self.view.sel()):
            pos = region.begin()
            try:
                open_tag = self.find_open_tag(pos)
                self.view.insert(edit, pos, '/%s>' % open_tag)
            except ValueError:
                self.view.insert(edit, pos, '/')

    def find_open_tag(self, end):
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
                # print('self-closing')
                continue

            # Handle close tag
            first_token = self.find_after('- comment', tag_begin)
            if self.view.substr(first_token) == '/':
                # print('close')
                depth += 1
                continue

            # Else, open tag

            if depth == 0:
                # print('found!')

                if self.view.match_selector(first_token, 'meta.tag.name'):
                    name_end = self.find_after('- meta.tag.name', first_token)
                    name_region = sublime.Region(first_token, name_end)
                    name = self.view.substr(name_region).strip()
                    # print('['+name+']')
                    return name
                else:
                    # Fragment, or invalid
                    return ''
            else:
                # print('open')
                depth -= 1
                continue

    def find_before(self, selector, pos):
        pos -= 1
        while pos >= 0:
            if self.view.match_selector(pos, selector):
                return pos
            else:
                pos -= 1
        
        raise ValueError("Can't find open tag.")

    def find_after(self, selector, pos):
        pos += 1
        max = self.view.size()
        while pos <= max:
            if self.view.match_selector(pos, selector):
                return pos
            else:
                pos += 1
        
        raise ValueError("Can't find open tag.")
