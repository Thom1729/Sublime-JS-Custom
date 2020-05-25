// SYNTAX TEST "Packages/User/JS Custom/Syntaxes/TypeScript.sublime-syntax"

/* Import/Export */

    import type T from 'somewhere';
//  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.import
//  ^^^^^^ keyword.control.import-export
//         ^^^^ keyword.control.import-export
//              ^ variable.other.readwrite
//                ^^^^ keyword.control.import-export
//                     ^^^^^^^^^^^ meta.string string.quoted.single

    import type { U, V } from 'somewhere';
//  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.import
//  ^^^^^^ keyword.control.import-export
//         ^^^^ keyword.control.import-export
//              ^^^^^^^^ meta.block
//                ^ variable.other.readwrite
//                 ^ punctuation.separator.comma
//                   ^ variable.other.readwrite
//                       ^^^^ keyword.control.import-export
//                            ^^^^^^^^^^^ meta.string string.quoted.single

    export type T = any;
//  ^^^^^^^^^^^^^^^^^^^ meta.export
//  ^^^^^^ keyword.control.import-export
//         ^^^^^^^^^^^^ meta.type-alias
//                     ^ punctuation.terminator.statement.empty - meta.export

/* Declarations */

    interface Foo {
//  ^^^^^^^^^^^^^^^^ meta.interface
//  ^^^^^^^^^ storage.type
//            ^^^ entity.name.interface
//                ^ meta.block punctuation.section.block.begin
        foo: any;
//^^^^^^^^^^^^^^^^ meta.interface meta.block
//      ^^^ variable.other.readwrite
//         ^ punctuation.separator.type
//           ^^^ meta.type support.type.any
//              ^ punctuation.separator
        bar?: any;
//^^^^^^^^^^^^^^^^^ meta.interface meta.block
//      ^^^ variable.other.readwrite
//         ^ storage.modifier.optional
//          ^ punctuation.separator.type
//            ^^^ meta.type support.type.any
//               ^ punctuation.separator
    }
//  ^ meta.block punctuation.section.block.end

    enum Foo {
//  ^^^^^^^^^^^ meta.enum
//  ^^^^ storage.type
//       ^^^ entity.name.enum
//           ^ punctuation.section.block.begin
        x,
//      ^ variable.other.readwrite
//       ^ punctuation.separator.comma
        y = 2,
//      ^ variable.other.readwrite
//        ^ keyword.operator.assignment
//          ^ constant.numeric.integer.decimal
//           ^ punctuation.separator.comma
    }
//  ^ meta.enum meta.block punctuation.section.block.end

    const enum Foo {}
//  ^^^^^ storage.type
//        ^^^^^^^^^^^ meta.enum
//        ^^^^ storage.type
//             ^^^ entity.name.enum

    declare enum Foo {}
//  ^^^^^^^ storage.type
//          ^^^^^^^^^^^ meta.enum
//          ^^^^ storage.type
//               ^^^ entity.name.enum

    type x < T > = any;
//  ^^^^^^^^^^^^^^^^^^ meta.type-alias
//  ^^^^ storage.type
//       ^ entity.name.type
//         ^^^^^ meta.generic
//               ^ keyword.operator.assignment
//                 ^^^ meta.type-alias support.type.any

    class Foo {
        foo: any = 42;
//      ^^^ variable.other.readwrite
//         ^ punctuation.separator.type
//           ^^^ meta.type support.type.any
//               ^ keyword.operator.assignment
    
        public foo;
//      ^^^^^^ storage.modifier
//             ^^^ variable.other.readwrite
        private foo;
//      ^^^^^^^ storage.modifier
//              ^^^ variable.other.readwrite
        protected foo;
//      ^^^^^^^^^ storage.modifier
//                ^^^ variable.other.readwrite
        readonly foo;
//      ^^^^^^^^ storage.modifier
//               ^^^ variable.other.readwrite

        private static foo;
//      ^^^^^^^ storage.modifier
//              ^^^^^^ storage.modifier
//                     ^^^ variable.other.readwrite

        foo(): any {}
//      ^^^^^^^^^^^ meta.function.declaration
//      ^^^ entity.name.function
//           ^ punctuation.separator.type
//             ^^^ meta.type support.type.any
//                 ^^ meta.function meta.block
    }

    abstract class Foo {}
//  ^^^^^^^^ storage.modifier
//           ^^^^^ meta.class storage.type.class

    namespace Foo {
//  ^^^^^^^^^^^^^^^^ meta.namespace
//  ^^^^^^^^^ storage.namespace
//            ^^^ entity.name.namespace
//                ^ meta.block punctuation.section.block.begin
    }
//  ^ meta.block punctuation.section.block.end

/* Annotations */

var x: any = 42;
//   ^ punctuation.separator.type
//     ^^^ meta.type support.type.any
//         ^^^^^^ - meta.type
//         ^ keyword.operator.assignment

let x: any = 42;
//   ^ punctuation.separator.type
//     ^^^ meta.type support.type.any
//         ^^^^^^ - meta.type
//         ^ keyword.operator.assignment

const x: any = 42;
//     ^ punctuation.separator.type
//       ^^^ meta.type support.type.any
//           ^^^^^^ - meta.type
//           ^ keyword.operator.assignment

let [ x: any = 42 ];
//     ^ punctuation.separator.type
//       ^^^ meta.type support.type.any
//           ^ keyword.operator.assignment

function f(x: any = 42) {}
//          ^ punctuation.separator.type
//            ^^^meta.type support.type.any
//                ^ keyword.operator.assignment

function f(readonly x) {}
//         ^^^^^^^^ storage.modifier
//                  ^ meta.binding.name variable.parameter.function

function f(x?: any) {}
//          ^ storage.modifier.optional
//           ^ punctuation.separator.type

function f(): any {}
//^^^^^^^^^^^^^^^^^^ meta.function
//^^^^^^ meta.function.declaration
//          ^ punctuation.separator.type
//            ^^^meta.type support.type.any
//                ^^ meta.block

function f ( x : any , ... y : any ) {}
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function.declaration
//         ^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function.declaration
//           ^ meta.binding.name variable.parameter.function
//             ^ punctuation.separator.type
//               ^^^ meta.type support.type.any
//                   ^ punctuation.separator.parameter.function
//                     ^^^ keyword.operator.spread
//                         ^ meta.binding.name variable.parameter.function
//                           ^ punctuation.separator.type
//                             ^^^ meta.type support.type.any

function f<T, U>() {}
//^^^^^^^^^^^^^^^^^^^ meta.function
//^^^^^^^^^^^^^^^^^ meta.function.declaration
//        ^^^^^^ meta.generic
//         ^ variable.parameter.generic
//          ^ punctuation.separator.comma
//            ^ variable.parameter.generic

function f(x): x is any {};
//^^^^^^^^^^^^^^^^^^^^^^^^ meta.function
//^^^^^^^^^^^^^^^^^^^^^^ meta.function.declaration
//           ^ punctuation.separator.type
//             ^^^^^^^^^ meta.type
//               ^^ keyword.operator.word
//                  ^^^ support.type.any

function f(this : any) {}
//         ^^^^ variable.language.this
//              ^ punctuation.separator.type
//                ^^^ support.type.any

    (x: any) => 42;
//  ^^^^^^^^^^^^^^ meta.function
//  ^^^^^^^^^^^ meta.function.declaration
//    ^ punctuation.separator.type
//      ^^^ meta.type support.type.any
//           ^^ storage.type.function.arrow

/* Assertions */

x as boolean;
//^^ keyword.operator.type
//   ^^^^^^^ meta.type support.type.primitive.boolean

    foo!.bar;
//     ^^ punctuation.accessor

/* Types */

let x: any;
//     ^^^ support.type.any
let x: void;
//     ^^^^ support.type.void
let x: never;
//     ^^^^^ support.type.never

let x: boolean;
//     ^^^^^^^ support.type.primitive.boolean
let x: number;
//     ^^^^^^ support.type.primitive.number
let x: string;
//     ^^^^^^ support.type.primitive.string
let x: null;
//     ^^^^ support.type.primitive.null
let x: undefined;
//     ^^^^^^^^^ support.type.primitive.undefined
let x: object;
//     ^^^^^^ support.type.primitive.object

let x: Foo;
//     ^^^ support.class

let x: any [ ];
//     ^^^^^^ meta.type
//     ^^^ support.type.any
//         ^ storage.modifier.array
//           ^ storage.modifier.array

let x: any [
//     ^^^^^^ meta.type
//     ^^^ support.type.any
//         ^ storage.modifier.array
    ];
//  ^ storage.modifier.array


let x: any
//     ^^^ meta.type support.type.any
    [];
//  ^^ meta.sequence punctuation.section.brackets - meta.type

let x: Foo<any, any>;
//     ^^^^^^^^^^^^^ meta.type
//     ^^^ support.class
//        ^^^^^^^^^^ meta.generic
//        ^ punctuation.definition.generic.begin
//         ^^^ support.type.any
//            ^ punctuation.separator.comma
//              ^^^ support.type.any
//                 ^ punctuation.definition.generic.end

let x: Foo
//     ^^^ meta.type support.class
    <;
//  ^ - meta.type


function f<T extends Foo>() {}
//        ^^^^^^^^^^^^^^^ meta.function.declaration meta.generic
//         ^ variable.parameter.generic
//           ^^^^^^^ storage.modifier.extends
//                   ^^^ support.class

let x: [any, any];
//     ^^^^^^^^^^ meta.type
//     ^^^^^^^^^^ meta.sequence
//     ^ punctuation.section.brackets.begin
//      ^^^ support.type.any
//         ^ punctuation.separator.comma
//           ^^^ support.type.any
//              ^ punctuation.section.brackets.end

let x: any & any;
//     ^^^^^^^^^ meta.type
//     ^^^ support.type.any
//         ^ keyword.operator.type.intersection
//           ^^^ support.type.any

let x: any | any;
//     ^^^^^^^^^ meta.type
//     ^^^ support.type.any
//         ^ keyword.operator.type.union
//           ^^^ support.type.any

let x: "a string";
//     ^ meta.type meta.string string.quoted.double

let x: 'a string';
//     ^ meta.type meta.string string.quoted.single

let x: 42;
//     ^^ meta.type constant.numeric.integer.decimal

let x: typeof Foo;
//     ^^^^^^^^^^ meta.type
//     ^^^^^ keyword.operator.type
//            ^^^ support.class
let x: keyof Foo;
//     ^^^^^^^^^ meta.type
//     ^^^^^ keyword.operator.type
//           ^^^ support.class

let x: Foo.bar;
//     ^^^^^^^ meta.type
//     ^^^ support.class
//        ^ punctuation.separator.accessor
//         ^^^ support.class

let x: {
//     ^ meta.type punctuation.section.block.begin

    a : any ,
//  ^ variable.other.readwrite
//    ^ punctuation.separator.type
//      ^^^ support.type.any
//          ^ punctuation.separator

    b ? : any ;
//  ^ variable.other.readwrite
//    ^ storage.modifier.optional
//      ^ punctuation.separator.type
//        ^^^ support.type.any
//            ^ punctuation.separator

    readonly c : any ;
//  ^^^^^^^^ storage.modifier
//           ^ variable.other.readwrite
//             ^ punctuation.separator.type
//               ^^^ support.type.any
//                   ^ punctuation.separator

    ( foo : any ) : any ;
//  ^ punctuation.section.group.begin
//    ^^^ meta.binding.name variable.parameter.function
//        ^ punctuation.separator.type
//          ^^^ support.type.any
//              ^ punctuation.section.group.end
//                ^ punctuation.separator.type
//                  ^^^ support.type.any
//                      ^ punctuation.separator


    <T>( foo : any ) : any ;
//  ^^^ meta.generic
//  ^ punctuation.definition.generic.begin
//   ^ meta.generic variable.parameter.generic
//    ^ punctuation.definition.generic.end
//     ^ punctuation.section.group.begin
//       ^^^ meta.binding.name variable.parameter.function
//           ^ punctuation.separator.type
//             ^^^ support.type.any
//                 ^ punctuation.section.group.end
//                   ^ punctuation.separator.type
//                     ^^^ support.type.any
//                         ^ punctuation.separator

    a ( foo : any ) : any ;
//  ^ variable.other.readwrite
//    ^ punctuation.section.group.begin
//      ^^^ meta.binding.name variable.parameter.function
//          ^ punctuation.separator.type
//            ^^^ support.type.any
//                ^ punctuation.section.group.end
//                  ^ punctuation.separator.type
//                    ^^^ support.type.any
//                        ^ punctuation.separator


    a <T>( foo : any ) : any ;
//  ^ variable.other.readwrite
//    ^^^ meta.generic
//    ^ punctuation.definition.generic.begin
//     ^ meta.generic variable.parameter.generic
//      ^ punctuation.definition.generic.end
//       ^ punctuation.section.group.begin
//         ^^^ meta.binding.name variable.parameter.function
//             ^ punctuation.separator.type
//               ^^^ support.type.any
//                   ^ punctuation.section.group.end
//                     ^ punctuation.separator.type
//                       ^^^ support.type.any
//                           ^ punctuation.separator

    new ( foo : any ) : any ;
//      ^ punctuation.section.group.begin
//        ^^^ meta.binding.name variable.parameter.function
//            ^ punctuation.separator.type
//              ^^^ support.type.any
//                  ^ punctuation.section.group.end
//                    ^ punctuation.separator.type
//                      ^^^ support.type.any
//                          ^ punctuation.separator

    new <T>( foo : any ) : any ;
//      ^^^ meta.generic
//      ^ punctuation.definition.generic.begin
//       ^ meta.generic variable.parameter.generic
//        ^ punctuation.definition.generic.end
//         ^ punctuation.section.group.begin
//           ^^^ meta.binding.name variable.parameter.function
//               ^ punctuation.separator.type
//                 ^^^ support.type.any
//                     ^ punctuation.section.group.end
//                       ^ punctuation.separator.type
//                         ^^^ support.type.any
//                             ^ punctuation.separator

    [ foo : string ] : any ;
//  ^^^^^^^^^^^^^^^^ meta.brackets
//  ^ punctuation.section.brackets.begin
//    ^^^ variable.other.readwrite
//        ^ punctuation.separator.type
//          ^^^^^^ support.type.primitive.string
//                 ^ punctuation.section.brackets.end
//                   ^ punctuation.separator.type
//                     ^^^ support.type.any
//                         ^ punctuation.separator

    [ foo : number ] : any ;
//  ^^^^^^^^^^^^^^^^ meta.brackets
//  ^ punctuation.section.brackets.begin
//    ^^^ variable.other.readwrite
//        ^ punctuation.separator.type
//          ^^^^^^ support.type.primitive.number
//                 ^ punctuation.section.brackets.end
//                   ^ punctuation.separator.type
//                     ^^^ support.type.any
//                         ^ punctuation.separator

    }
//  ^ meta.type punctuation.section.block.end

let x: ( foo ? : any ) => bar;
//     ^^^^^^^^^^^^^^^^^^^^^^ meta.type
//     ^^^^^^^^^^^^^^^ meta.group
//     ^ punctuation.section.group.begin
//       ^^^ variable.other.readwrite
//           ^ storage.modifier.optional
//             ^ punctuation.separator.type
//               ^^^ support.type.any
//                   ^ punctuation.section.group.end
//                     ^^ storage.type.function
//                        ^^^ support.class

let x: T extends U ? V : W;
//     ^^^^^^^^^^^^^^^^^^^ meta.type
//     ^ support.class
//       ^^^^^^^ keyword.operator.type.extends
//               ^ support.class
//                 ^ keyword.operator.type
//                   ^ support.class
//                     ^ keyword.operator.type
//                       ^ support.class
