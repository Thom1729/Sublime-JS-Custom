// SYNTAX TEST "Packages/User/JS Custom/Syntaxes/TypeScript.sublime-syntax"

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
//              ^ punctuation.terminator.statement
        bar?: any;
//^^^^^^^^^^^^^^^^^ meta.interface meta.block
//      ^^^ variable.other.readwrite
//         ^ storage.modifier.optional
//          ^ punctuation.separator.type
//            ^^^ meta.type support.type.any
//               ^ punctuation.terminator.statement
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
    }

    abstract class Foo {}
//  ^^^^^^^^ storage.modifier
//           ^^^^^ meta.class storage.type.class

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

let x: any[];
//     ^^^^^ meta.type
//     ^^^ support.type.any
//        ^^ storage.modifier.array

let x: Foo<any, any>;
//     ^^^^^^^^^^^^^ meta.type
//     ^^^ support.class
//        ^^^^^^^^^^ meta.generic
//        ^ punctuation.definition.generic.begin
//         ^^^ support.type.any
//            ^ punctuation.separator.comma
//              ^^^ support.type.any
//                 ^ punctuation.definition.generic.end

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

let x: keyof Foo;
//     ^^^^^^^^^ meta.type
//     ^^^^^ keyword.operator.type
//           ^^^ support.class

let x: Foo["bar"];
//     ^^^^^^^^^^ meta.type
//     ^^^ support.class
//        ^^^^^^^ meta.brackets
//         ^^^^^ meta.string string.quoted.double
