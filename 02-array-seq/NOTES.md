## Notes - Chapter 2, "An Array of Sequences"

- Grouping sequences by immutability 
    - Mutable sequences
        - list, bytearray, array.array, collections.deque, memoryview
        - tuple, str, and bytes\
- In Python, linebreaks inside of `[ ]`, `( )`, and `{ }` are ignored, so multi-line is fine
- List comprehension
    - `dummy = [str(x) for x in my_list]`
    - `x` in the listcomp is a local variable, so won't get clobbered