## Syntax Options

These options, specified in your `defaults` or in a named custom configuration, determine what features your custom syntaxes will have. Omitted options will be treated as `null`.

### ECMAScript Proposals

These options enable support for various [proposed language features](https://github.com/tc39/proposals). These proposals may change unexpectedly. If they stabilize, they will eventually be incorporated into the core JavaScript syntax and these extensions will be removed.

#### `es_pipeline`: boolean

Support the proposed [pipeline operator](https://github.com/tc39/proposal-pipeline-operator).

#### `es_slice`: boolean

Support the proposed [slice notation](https://github.com/gsathya/proposal-slice-notation).

### Third-party features

These extensions go beyond the base JavaScript syntax to support third-party features.

#### `jsx`: boolean

Highlight [JSX](https://reactjs.org/docs/introducing-jsx.html). (Uses the JSX extension extension from core.)

#### `typescript`: boolean

Highlight [TypeScript](http://typescriptlang.org). (Uses the TypeScript extension extension from core.)

Old-style type assertions (e.g. `<T>foo`) will be highlighted unless the `jsx` option is also enabled.

#### `flow_types`: boolean

Highlight [Flow type annotations](https://flow.org/en/docs/types/).

#### `eslint_directives`: boolean

Highlight [eslint configuration directives](https://eslint.org/docs/user-guide/configuring) in comments.

### Personalization

These extensions allow you to personalize your highlighting in various ways.

#### `string_object_keys`: boolean

Highlight unquoted object keys as strings, matching [babel-sublime](https://github.com/babel/babel-sublime)'s behavior.

#### `custom_templates`: object

Use custom syntax highlighting inside [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals). Several sub-options are available:

By default, the special `embed_configuration` disables this to avoid syntax recursion errors.

##### `default`: string

Highlight untagged template literals using a specified syntax. Example configuration:

```json
{
    "configurations": {
        "My Config": {
            "custom_templates": {
                "default": "scope:text.html.basic"
            }
        }
    }
}
```

This will highlight all untagged template literals as HTML. (The `comments` option below will override this when it applies.)

##### `tags`: object

Highlight tagged template literals based on the tag. Each key in `tag` should be a JavaScript identifier representing a template literal tag. The associated value should be a string specifying a context to include.

For example, to highlight template strings with the `style` tag as CSS, use the following configuration:

```json
{
    "configurations": {
        "My Config": {
            "custom_templates": {
                "tags": {
                    "style": "scope:source.css"
                }
            }
        }
    }
}
```

Then, if you use “JS Custom - My Config” to highlight the following code, the contents of this template literal will be highlighted as CSS:

```js
const myStyle = style`div { color: red }`;
```

##### `comments`: object

Highlight untagged template literals based on a preceding block comment. Example configuration:

```json
{
    "configurations": {
        "My Config": {
            "custom_templates": {
                "comments": {
                    "style": "scope:source.css"
                }
            }
        }
    }
}
```

Example JavaScript:

```js
const myStyle = /*style*/`div { color: red }`;
const myStyle = /* style */`div { color: red }`;
```

##### `lookaheads`: object

Highlight untagged template literals based on the contents. Example configuration:

```json
{
    "configurations": {
        "My Config": {
            "custom_templates": {
                "lookaheads": {
                    "select\\b": "scope:source.sql"
                }
            }
        }
    }
}
```

Example JavaScript:

```js
const myQuery = `select 1 from dual`;
```

##### `styled_components`: boolean

Highlight template string literals for [Styled Components](https://www.styled-components.com/).

##### `clear_all_scopes`: boolean

Inside custom template literals, clear all of the enclosing JavaScript scopes. Ordinarily, only the `string` scope will be cleared. Enable this option if you're using a third-party tool that requires it.

### Metadata

These options don't affect the syntax highlighting itself, but rather the way that Sublime uses the syntax.

#### `name`: string

The name of the syntax as it will appear in the syntax selector. (If this is omitted, the syntax will be named “JS Custom - <var>name</var>”, where <var>name</var> is the key in the `configurations` object.)

#### `scope`: string

The top-level scope that will be used for the syntax. (If this is omitted, the scope will be “source.js.<var>name</var>”, where <var>name</var> is based on the key in the `configurations` object.)

#### `file_extensions`: array

An array of file extensions. Files with the given extensions will use this syntax.

#### `hidden`: boolean

If this is `true`, the compiled syntax will not appear in the syntax menu or the command palette. It can still be referenced or included by other syntaxes.

#### `first_line_match`: string

Files whose first line matches the given regular expression will use this syntax.

### Deprecated

These options have been superseded by newer, more flexible options.

#### `custom_template_tags`

Superseded by `custom_templates.tags`.

#### `styled_components`

Superseded by `custom_templates.styled_components`.

#### `typescript.old_style_assertions`

Obsolete. Old-style type assertions will work unless JSX is enabled.
