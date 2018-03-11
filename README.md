# JS Custom

Customizable JavaScript syntax highlighting for Sublime Text supporting JSX, Flow, and more. You can use JS Custom as a drop-in replacement for [babel-sublime](https://github.com/babel/babel-sublime) or create your own customized syntax with exactly the features you need. Because JS Custom is based on the core JavaScript syntax, it will work with most tools written for the original — and as the original is updated and improved, JS Custom will inherit those improvements.

## Installation

JS Custom can be installed via [Package Control](https://packagecontrol.io/installation).

Alternatively, you can install JS Custom manually by cloning it into your Packages directory as “JSCustom”.

## Usage

JS Custom ships with two example configurations: “JS Custom - Default” and “JS Custom - React”. These should automatically be built and available for use upon installation.

To customize your syntaxes, choose Preferences &rarr; Package Settings &rarr; JS Custom &rarr; Settings from the menubar. The package default settings will be shown on the left; your user settings will be on the right. When you change your user settings, your custom syntaxes will automatically be recompiled. (This may take a few seconds, especially if you have a lot of configurations.)

If you modify your user settings outside Sublime Text, this package may not notice your modifications. You can force it to rebuild all of your custom syntaxes by choosing Preferences &rarr; Package Settings &rarr; JS Custom &rarr; Rebuild Syntaxes from the menubar, or by choosing “JS Custom: Rebuild Syntaxes” from the command palette.

## Configuration

The following options are available at the top level of your user settings:

### `configurations`: object

An object containing one or more named configurations. The keys should be the names you would like your custom configurations to have. The values are objects specifying [syntax options](#syntax-options).

### `defaults`: object

An object specifying default [syntax options](#syntax-options) that will apply to all of your syntaxes. Your named configurations will override these defaults.

### `auto_build`: boolean

If true, JS Custom will automatically rebuild your syntaxes when you modify your user settings. Only syntaxes whose configurations have changed will be rebuilt. If `auto_build` is disabled, you will have to run the rebuild command manually.

## Syntax Options

These options, specified in your `defaults` or in a named custom configuration, determine what features your custom syntaxes will have. Omitted options will be treated as `null`.

### `name`: string

The name of the syntax as it will appear in the syntax selector. (If this is omitted, the syntax will be named “JS Custom - <var>name</var>”, where <var>name</var> is the key in the `configurations` object.)

### `file_extensions`: array

An array of file extensions. Files with the given extensions will be use this syntax.

### `comma_operator`: boolean

Scope the [comma operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_Operator) `keyword.operator.comma`. Other uses of the comma, such as to separate array items or function arguments, will still be scoped `punctuation.separator.comma`.

### `es_decorators`: boolean

Highlight the experimental [decorator syntax](https://github.com/tc39/proposal-decorators). (When the decorators proposal advances, support will presumably be added in the core JavaScript syntax. At that time, this extension will be removed.)

### `string_object_keys`: boolean

Highlight unquoted object keys as strings, matching [babel-sublime](https://github.com/babel/babel-sublime)'s behavior.

### `jsx`: boolean

Highlight [JSX](https://reactjs.org/docs/introducing-jsx.html).

### `flow_types`: boolean

Highlight [Flow type annotations](https://flow.org/en/docs/types/).

### `eslint_directives`: boolean

Highlight [eslint configuration directives](https://eslint.org/docs/user-guide/configuring) in comments.

### `styled_components`: boolean

Highlight template string literals for [Styled Components](https://www.styled-components.com/).

### `custom_tagged_literals`: object

Highlight user-defined [tagged template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).

Each key in the given object should be a JavaScript identifier representing a template literal tag. The associated value should be a string specifying a context to include: for instance, `“scope:source.css”`

Example:

```json
{
    “configurations”: {
        “My Config”: {
            “custom_tagged_literals”: {
                “style”: “scope:source.css”
            }
        }
    }
}
```

Then, if you use “JS Custom - My Config” to highlight the following code, the contents of the template literal will be highlighted as CSS.

```js
const myStyle = style`div { color: red }`;
```

## Contributing

To request a feature or report a bug, create a new issue. All suggestions are welcome.

When reporting a bug, please include a code snippet that demonstrates the problem. If the bug exists in Sublime's core JavaScript syntax, it should be reported [here](https://github.com/sublimehq/Packages/issues) — but if you're not sure, then go ahead and post it here.

When requesting a new feature, please include a link to any relevant documentation. Because of the unique design of JS Custom, we can accommodate a variety of nonstandard features.
