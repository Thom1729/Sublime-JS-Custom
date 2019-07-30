// SYNTAX TEST "Packages/User/JS Custom/Tests/templates/templates.sublime-syntax"

    css`a { color: red; }`
//  ^^^ variable.function.tagged-template
//     ^^^^^^^^^^^^^^^^^^^ meta.string
//     ^ string.quoted.other punctuation.definition.string.begin
//      ^^^^^^^^^^^^^^^^^ source.css - string
//                       ^ string.quoted.other punctuation.definition.string.end
    `div { color: blue; }`;
//  ^^^^^^^^^^^^^^^^^^^^^^ meta.string
//  ^ string.quoted.other punctuation.definition.string.begin
//   ^^^^^^^^^^^^^^^^^^^^ source.css
//                       ^ string.quoted.other punctuation.definition.string.end

    other`text`;
//  ^^^^^ variable.function.tagged-template
//       ^^^^^^ meta.string string.quoted.other
//       ^ punctuation.definition.string.begin
//            ^ punctuation.definition.string.end

    styled`color: red`
//  ^^^^^^ variable.function.tagged-template
//        ^ string.quoted.other punctuation.definition.string.begin
//        ^^^^^^^^^^^^ meta.string
//         ^^^^^^^^^^ source.js.css - string
//         ^^^^^ meta.property-name support.type.property-name
//              ^ punctuation.separator.key-value
//                ^^^ meta.property-value support.constant.color.w3c-standard-color-name
//                   ^ string.quoted.other punctuation.definition.string.end
    `color: blue`;
//  ^^^^^^^^^^^^^ meta.string
//  ^ string.quoted.other punctuation.definition.string.begin
//   ^^^^^^^^^^^ source.js.css - string
//              ^ string.quoted.other punctuation.definition.string.end
