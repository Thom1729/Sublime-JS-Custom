# Recipes

These example configurations are designed to support common use cases. You can customize these configurations or combine options from several, or you can create multiple configurations for different projects or use cases.

## JSX

```json
{
    "configurations": {
        "JSX Recipe": {
            "jsx": true
        }
    }
}
```

## TypeScript

```json
{
    "configurations": {
        "TypeScript Recipe": {
            "typescript": true
        }
    }
}
```

## TSX

```json
{
    "configurations": {
        "TSX Recipe": {
            "jsx": true,
            "typescript": true
        }
    }
}
```

## Styled Components

For Styled Components version 5.

```json
{
    "configurations": {
        "Styled Components Recipe": {
            "custom_templates": {
                "styled_components": true,
                "tags": {
                    "css": "scope:source.js.css",
                    "createGlobalStyle": "scope:source.css", // v4 and above
                    "injectGlobal": "scope:source.css", // before v4
                }
            }
        }
    }
}
```

## Emotion.js

```json
{
    "configurations": {
        "Emotion.js Recipe": {
            "custom_templates": {
                "styled_components": true, // If you use @emotions/styled
                "tags": {
                    "css": "scope:source.js.css",
                }
            }
        }
    }
}
```

## Highlight HTML in template strings

Highlight template strings as HTML if they begin with a `<`:

```json
{
    "configurations": {
        "HTML Lookahead Recipe": {
            "custom_templates": {
                "lookaheads": {
                    // To highlight `<div>Hello, World!</div>`
                    "<": "scope:text.html.basic",
                },
                "comments": {
                    // To highlight `/*html*/<div>Hello, World!</div>`
                    "html": "scope:text.html.basic",
                },
                "tags": {
                    // To highlight `html<div>Hello, World!</div>`
                    "html": "scope:text.html.basic",
                }
            }
        }
    }
}
```
