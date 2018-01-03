WARNING: This is a prerelease package under development. It may not work and the documentation is more optimistic than descriptive. The official release will be posted in the [Sublime Text forum](https://forum.sublimetext.com).

# JS Custom

Customizable JavaScript syntax highlighting for Sublime Text.

## Features

- Support for JSX, Flow types, and more.
- User-configurable: turn features on and off at will.
- Create multiple customized syntaxes for different projects.
- Based directly on Sublime's built-in JavaScript highlighting.

## Installation

JS Custom can be installed via [Package Control](https://packagecontrol.io/installation). Restart Sublime Text after installation.

## Usage

JS Custom ships with two example configurations: "JS Custom - Default" and "JS Custom - React". These should automatically be built and available for use upon installation.

To customize your syntaxes, choose Preferences &rarr; Package Settings &rarr; JS Custom &rarr; Settings from the menubar. The package default settings will be shown on the left; your user settings will be on the right. When you change your user settings, your custom syntaxes will automatically be recompiled. (This may take a few seconds, especially if you have a lot of configurations.)

If you modify your user settings outside Sublime Text, this package may not notice your modifications. You can force it to rebuild all of your custom syntaxes by choosing Preferences &rarr; Package Settings &rarr; JS Custom &rarr; Rebuild Syntaxes from the menubar, or by choosing "JS Custom: Rebuild Syntaxes" from the command palette.

## Configuration

The following options are available at the top level of your user settings:

### `configurations`

An object containing one or more named configurations. The keys should be the names you would like your custom configurations to have. The values are objects specifying [syntax options](#syntax-options).

### `defaults`

An object specifying default [syntax options](#syntax-options) that will apply to all of your syntaxes. Your named configurations will override these defaults.

## Syntax Options

These options, specified in your `defaults` or in a named custom configuration, determine what features your custom syntaxes will have. Omitted options will be treated as `null`.

### `name`: string

The name of the syntax as it will appear in the syntax selector. (If this is omitted, the syntax will be named "JS Custom - <var>name</var>", where <var>name</var> is the key in the `configurations` object.)

### `comma_operator`: boolean

Scope the [comma operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_Operator) `keyword.operator.comma`. Other uses of the comma, such as to separate array items or function arguments, will still be scoped `punctuation.separator.comma`.

### `jsx`: boolean

Highlight [JSX](https://reactjs.org/docs/introducing-jsx.html).

### `flow_types`: boolean

Highlight [Flow type annotations](https://flow.org/en/docs/types/).

### `custom_tagged_literals`: object

Highlight user-defined [tagged template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).

Each key in the given object should be a JavaScript identifier representing a template literal tag. The associated value should be a string specifying a context to include: for instance, `"scope:source.css"`

Example:

```json
{
    "configurations": {
        "My Config": {
            "custom_tagged_literals": {
                "style": "scope:source.css"
            }
        }
    }
}
```

Then, if you use "JS Custom (My Config)" to highlight the following code, the contents of the template literal will be highlighted as CSS.

```js
const myStyle = style`div { color: red }`;
```
