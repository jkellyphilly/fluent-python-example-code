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

### Slicing
It's possible to name your slices like `SKU = slice(0, 6)` and then use those as replacements for the `X:Y:Z` nomenclature of slicing. 
```
>>> item[SKU] 
```
(similar to `item[0:6]`)

Look into using ellipsis in slice objects - in NumPy it's a shortcut for grabbing "all" (i.e. `:`) for the other dimesions (since sometimes more than 2D).

- Mutable sequences can be graftted, excised, and otherwise modified in place using slice notation. See `slice_examples.py`
- So, `l[2:5] = [20, 30]` is replacing elements 2-4 (5 not included) in `l` with an iterable of `[20, 30]`

### Building a list of lists
Woah - this is cool. Look at the example of `list_of_lists_example.py`

TLDR - using a listcomp actually does what we want, becuase each list generated in the listcomp is treated like a local variable. If we use `*` with a sequence - it is the same sequence duplicated multiple times. 

NOTE: `id()` is a method to get the ID of a variable. If you use `*=` on a mutable sequence, the variable has the same `id` before and after the operation. HOWEVER, if you use it on an immutable sequence, a new object is produced (different `id`s). 