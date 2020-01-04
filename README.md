# JS Custom

Customizable JavaScript syntax highlighting for Sublime Text supporting JSX, Flow, and more. You can use JS Custom as a drop-in replacement for [babel-sublime](https://github.com/babel/babel-sublime) or create your own customized syntax with exactly the features you need. Because JS Custom is based on the core JavaScript syntax, it will work with most tools written for the original — and as the original is updated and improved, JS Custom will inherit those improvements.

## Installation

JS Custom can be installed via [Package Control](https://packagecontrol.io/installation).

Alternatively, you can install JS Custom manually by cloning it into your Packages directory as “JSCustom”. If you do, you may need to manually install its dependencies.

## Usage

JS Custom ships with two example configurations: “JS Custom - Default” and “JS Custom - React”. These should automatically be built and available for use upon installation.

To customize your syntaxes, choose Preferences → Package Settings → JS Custom → Settings from the menubar. The package default settings will be shown on the left; your user settings will be on the right. When you change your user settings, your custom syntaxes will automatically be recompiled. (This may take a few seconds, especially if you have a lot of configurations.)

If you modify your user settings outside Sublime Text, this package may not notice your modifications. You can force it to rebuild all of your custom syntaxes by choosing Preferences → Package Settings → JS Custom → Rebuild Syntaxes from the menubar, or by choosing “JS Custom: Rebuild Syntaxes” from the command palette.

## Commands

JS Custom provides the following commands. Except for “JSX Close Tag”, they are available in the command palette and under Preferences → Package Settings → JS Custom.

### JS Custom: Rebuild Syntaxes (`build_js_custom_syntaxes`)

Rebuild all of your custom syntaxes and remove any obsolete compiled syntaxes.

This command takes an optional `versions` argument accepting a list of configuration names. If you pass `versions`, only the specified configurations will be rebuilt.

### JS Custom: Clear User Data (`clear_js_custom_user_data`)

Remove the `Packages/User/JS Custom` directory, including all compiled syntaxes.

### Preferences: JS Custom

Open the default JS Custom preferences and your own JS Custom user preferences side-by-side in a new window (using the built-in `edit_settings` command).

### JSX Close Tag (`jsx_close_tag`)

As the built-in `close_tag` command, but should work for JSX tags.

This command is not available in the command palette or the JS Custom menu. By default, whenever you run the `close_tag` command in a JavaScript file, then the `jsx_close_tag` command will be run instead. You can disable this with the `jsx_close_tag` setting.

## Configuration

The following options are available at the top level of your user settings:

### `configurations`: object

An object containing one or more named configurations. The keys should be the names you would like your custom configurations to have. The values are objects specifying [syntax options](#syntax-options).

### `defaults`: object

An object specifying default [syntax options](#syntax-options) that will apply to all of your syntaxes. Your named configurations will override these defaults.

### `embed_configuration`: object

An object specifying a configuration to use when another syntax embeds the `source.js` scope.

### `auto_build`: boolean

If true, JS Custom will automatically rebuild your syntaxes when you modify your user settings. Only syntaxes whose configurations have changed will be rebuilt. If `auto_build` is disabled, you will have to run the rebuild command manually.

### `jsx_close_tag`: boolean

If true, when you run the `close_tag` command in a JavaScript file, this package's `jsx_close_tag` command will be invoked instead.

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

Highlight [JSX](https://reactjs.org/docs/introducing-jsx.html).

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

An array of file extensions. Files with the given extensions will be use this syntax.

#### `hidden`: boolean

If this is `true`, the compiled syntax will not appear in the syntax menu or the command palette. It can still be referenced or included by other syntaxes.

### Deprecated

These options have been superseded by newer, more flexible options.

#### custom_template_tags

Superseded by `custom_templates.tags`.

#### styled_components

Superseded by `custom_templates.styled_components`.

## Frequently Asked Questions

### My syntaxes don't appear in the syntax selection menu. Where are they?

They are in the syntax selection menu under "User". It would be nice to have them listed under "JS Custom", but when generating that menu Sublime only looks at the physical location of the syntax definition files, and JS Custom compiles them to `User/JS Custom/Syntaxes`.

### I've switched from Babel-sublime and my code looks different. How do I restore the old appearance?

If you want unquoted object keys to be highlighted as strings, set the `string_object_keys` configuration option to `true`.

Other than that, the differences occur when Babel-sublime's syntax does not conform to the [scope naming guidelines](https://www.sublimetext.com/docs/3/scope_naming.html) or other best practices. If you liked the old appearance, then rather than modifying the syntax itself I would suggest modifying your theme. You can find further discussion [here](https://github.com/Thom1729/Sublime-JS-Custom/issues/22).

## Contributing

To request a feature or report a bug, create a new issue. All suggestions are welcome.

When reporting a bug, please include a code snippet that demonstrates the problem. If the bug exists in Sublime's core JavaScript syntax, it should be reported [here](https://github.com/sublimehq/Packages/issues) — but if you're not sure, then go ahead and post it here.

When requesting a new feature, please include a link to any relevant documentation. Because of the unique design of JS Custom, we can accommodate a variety of nonstandard features.
