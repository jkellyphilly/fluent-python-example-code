## Notes - Chapter 2, "An Array of Sequences"

- Grouping sequences by immutability 
    - Mutable sequences
        - list, bytearray, array.array, collections.deque, memoryview
        - tuple, str, and bytes\
- In Python, linebreaks inside of `[ ]`, `( )`, and `{ }` are ignored, so multi-line is fine

### List comprehension
    - `dummy = [str(x) for x in my_list]`
    - `x` in the listcomp is a local variable, so won't get clobbered

Can think of listcomps like nested for loops for some examples:
```
tshirts = [(color, size) for size in sizes for color in colors]
```

This is the same as:
```
tshirts = [(color, size) for size in sizes 
                         for color in colors]
```

Which is also the same as:
```
for size in sizes:
    for color in colors:
        #populate list here
```

### GenExps (Generator Expressions)
Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than brackets.

Example:
```
symbols = <some non-ASCII stuff here>
tuple(ord(symbol) for symbol in symbols)
```

NOTE: genexp feeds the `for` loop producing one item at a time. It doesn't build the list to populate (like a listcomp does) from the get-go; so the genexp feeds one item at a time and appends to the final result (list, array, local variable in a different function, whatever)