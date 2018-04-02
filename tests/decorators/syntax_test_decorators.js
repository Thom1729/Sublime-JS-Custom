// SYNTAX TEST "Packages/User/JS Custom/Tests/jsx/jsx.sublime-syntax"

class Foo {

    @foo bar() {}
//  ^^^^ meta.annotation
//  ^ punctuation.definition.annotation
//   ^^^ variable.annotation
//       ^^^ entity.name.function

    @foo.bar bar() {}
//  ^^^^^^^^ meta.annotation
//  ^ punctuation.definition.annotation
//   ^^^ variable.other.object - variable.annotation
//       ^^^ variable.annotation
//           ^^^ entity.name.function

    @(whatever) bar() {}
//  ^^^^^^^^^^^ meta.annotation
//  ^ punctuation.definition.annotation
//   ^^^^^^^^^^ meta.group
//              ^^^ entity.name.function
}

    @foo class Foo {}
//  ^^^^ meta.annotation
//  ^ punctuation.definition.annotation
//   ^^^ variable.annotation
//       ^^^^^ storage.type.class

    @foo.bar class Foo {}
//  ^^^^^^^^ meta.annotation
//  ^ punctuation.definition.annotation
//   ^^^ variable.other.object - variable.annotation
//       ^^^ variable.annotation
//           ^^^^^ storage.type.class

    @(whatever) class Foo {}
//  ^^^^^^^^^^^ meta.annotation
//  ^ punctuation.definition.annotation
//   ^^^^^^^^^^ meta.group
//              ^^^^^ storage.type.class
