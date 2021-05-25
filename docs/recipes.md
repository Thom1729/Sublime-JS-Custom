# Recipes

These example configurations are designed to support common use cases. You can customize these configurations or combine options from several, or you can create multiple configurations for different projects or use cases.

- [JSX](#jsx)
- [TypeScript](#typescript)
- [TSX](#tsx)
- [Styled Components](#styled-components)
- [Emotion.js](#emotionjs)
- [Apollo / Prisma / GraphQL gql Tag](#apollo--prisma--graphql-gql-tag)
- [Highlight HTML in template strings](#highlight-html-in-template-strings)

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

## Apollo / Prisma / GraphQL gql Tag

you need to also install Sublime Text package for GraphQL syntax definition.

```json
{
    "configurations": {
        "GraphQL Recipe": {
            "custom_templates": {
                // if you use something like:
                // const fragment = gql`
                //     fragment User on User {
                //     ...
                // `;
                "tags": {
                    "gql": "scope:source.graphql",
                },
                // if you use something like:
                // const fragment = /* GraphQL */`
                //     fragment User on User {
                //     ...
                // `;
                "comments": {
                    "GraphQL": "scope:source.graphql",
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
