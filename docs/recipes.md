# Recipes

These example configurations are designed to support common use cases. You can customize these configurations or combine options from several, or you can create multiple configurations for different projects or use cases.

- [JSX](#jsx)
- [TypeScript](#typescript)
- [TSX](#tsx)
- [Styled Components](#styled-components)
- [Emotion.js](#emotionjs)
- [GraphQL](#graphql)
- [Highlight HTML in template strings](#highlight-html-in-template-strings)

## JSX

```js
{
    "configurations": {
        "JSX Recipe": {
            "jsx": true
        }
    }
}
```

## TypeScript

```js
{
    "configurations": {
        "TypeScript Recipe": {
            "typescript": true
        }
    }
}
```

## TSX

```js
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

```js
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

```js
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

## GraphQL

Requires the [GraphQL](https://github.com/dncrews/GraphQL-SublimeText3) package.

```js
{
    "configurations": {
        "GraphQL Recipe": {
            "custom_templates": {
                "tags": {
                    // If you use GraphQL tags:
                    // const fragment = gql`
                    //     fragment User on User {
                    //     …
                    // `;
                    "gql": "scope:source.graphql",
                },
                "comments": {
                    // const fragment = /* GraphQL */`
                    //     fragment User on User {
                    //     ...
                    // `;
                    "GraphQL": "scope:source.graphql",
                }
            }
        }
    }
}
```

## Highlight HTML in template strings

Highlight template strings as HTML if they begin with a `<`:

```js
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
