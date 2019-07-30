// SYNTAX TEST "Packages/User/JS Custom/Tests/templates/templates.sublime-syntax"

    css`a { color: red; }`
//  ^^^ variable.function.tagged-template
//     ^ string.template punctuation.definition.string.template.begin
//      ^^^^^^^^^^^^^^^^^ source.css - string
//                       ^ string.template punctuation.definition.string.template.end
    `div { color: blue; }`;
//  ^ string.template punctuation.definition.string.template.begin
//   ^^^^^^^^^^^^^^^^^^^^ source.css
//                       ^ string.template punctuation.definition.string.template.end

    other`text`;
//  ^^^^^ variable.function.tagged-template
//       ^^^^^^ string.template
//       ^ punctuation.definition.string.begin
//            ^ punctuation.definition.string.end

    styled`color: red`
//  ^^^^^^ variable.function.tagged-template
//        ^ string.template punctuation.definition.string.template.begin
//         ^^^^^^^^^^ source.js.css - string
//         ^^^^^ meta.property-name support.type.property-name
//              ^ punctuation.separator.key-value
//                ^^^ meta.property-value support.constant.color.w3c-standard-color-name
//                   ^ string.template punctuation.definition.string.template.end
    `color: blue`;
//  ^ string.template punctuation.definition.string.template.begin
//   ^^^^^^^^^^^ source.js.css - string
//              ^ string.template punctuation.definition.string.template.end
