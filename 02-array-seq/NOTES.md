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

### Tuple Unpacking
```
>> lax_coordinates = (x, y)
>> latitude, longitude = lax_coordinates 
``` 

Can use a star (*) in a function call to unpack the tuple when the function is initiated. 
```
>> t = (20, 8)
>> divmod(*t)
(2, 4)
```

Can also use a star to grab any number of items. Examples:
```
>> a, b, *rest = range(5)
>> a, b, rest
(0, 1, [2, 3, 4])

>> a, b, *rest = range(3)
>> a, b, rest
(0, 1, [2])

>> *head, b, c, d = range(5)
>> head, b, c, d
([0, 1], 2, 3, 4)
```

### Named tuples
See `named_tuples_example.py`. Basically if you define a class name and a list of field names (in the right order), you can access the fields by name (or position). 
- `_fields` is a tuple with the field names of the class
- `_make()` allows you to instantiate a named tuple from an iterable (`City(*delhi_data)` would do the same)

