
({
    foo: 42,
//  ^^^ meta.group meta.mapping meta.mapping.key string.unquoted

    [bar]: 42,
//  ^^^^^ - string
});

const { x } = 42;
//      ^ - string

const { x: y } = 42;
//      ^ string.unquoted
