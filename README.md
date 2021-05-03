# JS Custom

Customizable JavaScript syntax highlighting for Sublime Text supporting JSX, Flow, and more. You can use JS Custom as a drop-in replacement for [babel-sublime](https://github.com/babel/babel-sublime) or create your own customized syntax with exactly the features you need. Because JS Custom is based on the core JavaScript syntax, it will work with most tools written for the original — and as the original is updated and improved, JS Custom will inherit those improvements.

## Installation

JS Custom can be installed via [Package Control](https://packagecontrol.io/installation). If JS Custom is uninstalled, it will remove any compiled syntax definitions.

## Usage

To use JS Custom, you specify one or more syntax configurations in the JS Custom preferences. JS Custom will compile each configuration into a syntax definition. By default, JS Custom provides two example syntax configurations: “JS Custom - Default” and “JS Custom - React”. These should automatically be compiled and available for use upon installation.

All syntaxes compiled by JS Custom are created inside your User package. They are found in the Syntax menu under “User”, not under “JS Custom”.

## Configuration

To customize your syntax configurations, choose Preferences → Package Settings → JS Custom → Settings from the menubar. The package default settings will be shown on the left and your user settings on the right. When you change your user settings, your custom syntaxes will automatically be recompiled. (This may take a few seconds, especially if you have a lot of syntax configurations.)

A number of common example syntax configurations can be found in the [Recipes](./docs/recipes.md). See also the [Configuration Reference](./docs/configuration.md).

If you modify your user settings outside Sublime Text, this package may not notice your modifications. To manually rebuild all of your custom syntaxes, choose Preferences → Package Settings → JS Custom → Rebuild Syntaxes from the menubar or choose “JS Custom: Rebuild Syntaxes” from the command palette.

## Commands

JS Custom provides the following commands. Except for “JSX Close Tag”, they are available in the command palette and under Preferences → Package Settings → JS Custom.

### Preferences: JS Custom

Open the default JS Custom preferences and your own JS Custom user preferences side-by-side in a new window.

### JS Custom: Rebuild Syntaxes (`build_js_custom_syntaxes`)

Rebuild all of your custom syntaxes and remove any obsolete compiled syntaxes.

This command takes an optional `versions` argument accepting a list of configuration names. If you pass `versions`, only the specified configurations will be rebuilt.

### JS Custom: Clear User Data (`clear_js_custom_user_data`)

Remove the `Packages/User/JS Custom` directory, including all compiled syntaxes.

### JSX Close Tag (`jsx_close_tag`)

As the built-in `close_tag` command, but should work for JSX tags.

This command is not available in the command palette or the JS Custom menu. By default, whenever you run the `close_tag` command in a JavaScript file, then the `jsx_close_tag` command will be run instead. You can disable this with the `jsx_close_tag` setting.

## Frequently Asked Questions

### My syntaxes don't appear in the syntax selection menu. Where are they?

They are in the syntax selection menu under "User". It would be nice to have them listed under "JS Custom", but when generating that menu Sublime only looks at the physical location of the syntax definition files, and JS Custom compiles them to `User/JS Custom/Syntaxes`.

### I've switched from the [Babel package](https://github.com/babel/babel-sublime) and my code looks different. How do I restore the old appearance?

The current version of babel-sublime is built using JS Custom with the following configuration:

```json
{
    "name": "JavaScript (Babel)",
    "scope": "source.js",
    "file_extensions": [ "js", "jsx", "es6", "babel" ],
    "flow_types": true,
    "jsx": true,
    "string_object_keys": true,
    "custom_templates": {
        "styled_components": true,
    }
}
```

## Contributing

To request a feature or report a bug, create a new issue. All suggestions are welcome.

When reporting a bug, please include a code snippet that demonstrates the problem. If the bug exists in Sublime's core JavaScript, JSX, or TypeScript syntax, it should be reported [here](https://github.com/sublimehq/Packages/issues) — but if you're not sure, then go ahead and post it here.

When requesting a new feature, please include a link to any relevant documentation. Because of the unique design of JS Custom, we can accommodate a variety of nonstandard features.
