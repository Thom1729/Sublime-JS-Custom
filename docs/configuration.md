# Configuration

The following options are available at the top level of your user settings:

## `configurations`: object

An object containing one or more named configurations. The keys should be the names you would like your custom configurations to have. The values are objects specifying [syntax options](#syntax-options).

## `defaults`: object

An object specifying default [syntax options](#syntax-options) that will apply to all of your syntaxes. Your named configurations will override these defaults.

## `embed_configuration`: object

An object specifying a configuration to use when another syntax embeds the `source.js` scope.

## `auto_build`: boolean

If true, JS Custom will automatically rebuild your syntaxes when you modify your user settings. Only syntaxes whose configurations have changed will be rebuilt. If `auto_build` is disabled, you will have to run the rebuild command manually.

## `jsx_close_tag`: string or boolean

When you run the `close_tag` command, if the scope of the file matches this selector, then this package's `jsx_close_tag` command will be invoked instead. You may have to modify this setting if you use the `scope` configuration option

If false, `jsx_close_tag` will never be run.

## `reassign_when_deleting`: string or `false`

When you remove a custom configuration, JS Custom will automatically find any views using that configuration and assign them to this default syntax so that Sublime won't show an error popup. You can set this setting to the path or scope of any syntax definition, or set it to `false` to disable the feature entirely.

# Syntax Options

These options, specified in your `defaults` or in a named custom configuration, determine what features your custom syntaxes will have. Omitted options will be treated as `null`.

## ECMAScript Proposals

These options enable support for various [proposed language features](https://github.com/tc39/proposals). These proposals may change unexpectedly. If they stabilize, they will eventually be incorporated into the core JavaScript syntax and these extensions will be removed.

### `es_pipeline`: boolean

Support the proposed [pipeline operator](https://github.com/tc39/proposal-pipeline-operator).

### `es_slice`: boolean

Support the proposed [slice notation](https://github.com/gsathya/proposal-slice-notation).

## Third-party features

These extensions go beyond the base JavaScript syntax to support third-party features.

### `jsx`: boolean

Highlight [JSX](https://reactjs.org/docs/introducing-jsx.html). (Uses the JSX extension extension from core.)

### `typescript`: boolean

Highlight [TypeScript](http://typescriptlang.org). (Uses the TypeScript extension extension from core.)

Old-style type assertions (e.g. `<T>foo`) will be highlighted unless the `jsx` option is also enabled.

### `flow_types`: boolean

Highlight [Flow type annotations](https://flow.org/en/docs/types/).

### `eslint_directives`: boolean

Highlight [eslint configuration directives](https://eslint.org/docs/user-guide/configuring) in comments.

## Personalization

These extensions allow you to personalize your highlighting in various ways.

### `string_object_keys`: boolean

Highlight unquoted object keys as strings, matching [babel-sublime](https://github.com/babel/babel-sublime)'s behavior.

### `custom_templates`: object

Use custom syntax highlighting inside [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals). Several sub-options are available:

By default, the special `embed_configuration` disables this to avoid syntax recursion errors.

#### `tags`: object

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

#### `comments`: object

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

#### `lookaheads`: object

Highlight untagged template literals based on the contents. Example configuration:

```json
{
    "configurations": {
        "My Config": {
            "custom_templates": {
                "lookaheads": {
                    "select\b": "scope:source.sql"
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

#### `styled_components`: boolean

Highlight template string literals for [Styled Components](https://www.styled-components.com/).

#### `clear_all_scopes`: boolean

Inside custom template literals, clear all of the enclosing JavaScript scopes. Ordinarily, only the `string` scope will be cleared. Enable this option if you're using a third-party tool that requires it.

## Metadata

These options don't affect the syntax highlighting itself, but rather the way that Sublime uses the syntax.

### `name`: string

The name of the syntax as it will appear in the syntax selector. (If this is omitted, the syntax will be named “JS Custom - <var>name</var>”, where <var>name</var> is the key in the `configurations` object.)

### `scope`: string

The top-level scope that will be used for the syntax. (If this is omitted, the scope will be “source.js.<var>name</var>”, where <var>name</var> is based on the key in the `configurations` object.)

### `file_extensions`: array

An array of file extensions. Files with the given extensions will be use this syntax.

### `hidden`: boolean

If this is `true`, the compiled syntax will not appear in the syntax menu or the command palette. It can still be referenced or included by other syntaxes.

## Deprecated

These options have been superseded by newer, more flexible options.

### `custom_template_tags`

Superseded by `custom_templates.tags`.

### `styled_components`

Superseded by `custom_templates.styled_components`.

### `typescript.old_style_assertions`

Obsolete. Old-style type assertions will work unless JSX is enabled.
