// SYNTAX TEST "Packages/User/JS Custom/Syntaxes/TypeScript.sublime-syntax"

    < T > foo;
//  ^^^^^ meta.assertion
//  ^ punctuation.definition.assertion.begin
//    ^ support.class
//      ^ punctuation.definition.assertion.end
//        ^^^ variable.other.readwrite

    foo < T > bar;
//  ^^^ variable.other.readwrite
//      ^ keyword.operator.relational
//        ^ variable.other.constant
//          ^ keyword.operator.relational
//            ^^^ variable.other.readwrite

    foo
    < T > bar;
//  ^ keyword.operator.relational
//    ^ variable.other.constant
//      ^ keyword.operator.relational
//        ^^^ variable.other.readwrite
