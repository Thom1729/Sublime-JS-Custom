
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

    `select * from dual`;
//  ^^^^^^^^^^^^^^^^^^^^ meta.string
//  ^ string.quoted.other punctuation.definition.string.begin
//   ^^^^^^^^^^^^^^^^^^ source.sql - string
//                     ^ string.quoted.other punctuation.definition.string.end

    /*css*/`a { color: red; }`
//  ^^^^^^^ comment.block
//         ^^^^^^^^^^^^^^^^^^^ meta.string
//          ^^^^^^^^^^^^^^^^^ source.css - string

    /* css */`a { color: red; }`
//  ^^^^^^^^^ comment.block
//           ^^^^^^^^^^^^^^^^^^^ meta.string
//            ^^^^^^^^^^^^^^^^^ source.css - string
    `div { color: blue; }`;
//  ^^^^^^^^^^^^^^^^^^^^^^ meta.string
//   ^^^^^^^^^^^^^^^^^^^^ source.css - string

    `<foo></foo>`;
//  ^^^^^^^^^^^^^ meta.string
//   ^^^^^^^^^^^ text.html.basic - string
