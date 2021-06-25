
    styled`color: red`
//  ^^^^^^ variable.function.tagged-template
//        ^ string.quoted.other punctuation.definition.string.begin
//        ^^^^^^^^^^^^ meta.string
//         ^^^^^^^^^^ source.js.css - string
//         ^^^^^ meta.property-name support.type.property-name
//              ^ punctuation.separator.key-value
//                ^^^ meta.property-value support.constant.color
//                   ^ string.quoted.other punctuation.definition.string.end
    `color: blue`;
//  ^^^^^^^^^^^^^ meta.string
//  ^ string.quoted.other punctuation.definition.string.begin
//   ^^^^^^^^^^^ source.js.css - string
//              ^ string.quoted.other punctuation.definition.string.end


    styled.div`color: red`;
//  ^^^^^^ variable.other
//        ^ punctuation.accessor.dot
//         ^^^ variable.function.tagged-template
//            ^^^^^^^^^^^^ meta.string
//            ^ punctuation.definition.string.begin
//             ^^^^^^^^^^ source.js.css - string
//             ^^^^^ meta.property-name support.type.property-name
//                  ^ punctuation.separator.key-value
//                    ^^^ meta.property-value support.constant.color
//                       ^ punctuation.definition.string.end

    styled.div.attrs({})`color: red`;
//                      ^^^^^^^^^^^^ meta.string
//                      ^ punctuation.definition.string.begin
//                       ^^^^^^^^^^ source.js.css - string
//                       ^^^^^ meta.property-name support.type.property-name
//                            ^ punctuation.separator.key-value
//                              ^^^ meta.property-value support.constant.color
//                                 ^ punctuation.definition.string.end

    styled(Foo)`color: red`;
//             ^^^^^^^^^^^^ meta.string
//             ^ punctuation.definition.string.begin
//              ^^^^^^^^^^ source.js.css - string
//              ^^^^^ meta.property-name support.type.property-name
//                   ^ punctuation.separator.key-value
//                     ^^^ meta.property-value support.constant.color
//                        ^ punctuation.definition.string.end