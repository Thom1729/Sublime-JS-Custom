// SYNTAX TEST "Packages/User/JS Custom/Tests/jsx/jsx.sublime-syntax"

foo[1:2:3];
// ^^^^^^^ meta.brackets
//   ^ punctuation.separator.slice
//     ^ punctuation.separator.slice
//       ^ punctuation.section.brackets

foo[true ? 1 : 2 : 3];
// ^^^^^^^^^^^^^^^^^^ meta.brackets
//           ^ keyword.operator.ternary
//               ^ punctuation.separator.slice
