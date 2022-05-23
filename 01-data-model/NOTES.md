## Notes - Chapter 1, "The Python Data Model"

- Pull from the rich methods that already exist in Python and make your class/module methods "Pythonic"
    - Example is len(<FrenchDeck instance>) from Example 1-1 (`frenchdeck.py`)
- Ohhh SHIT. Cool - because `__getitem__` for a `FrenchDeck` instance delegates to our `_cards` variable, we can call something that uses `__getitem__` (like slicing) on our `FrenchDeck` instance... without any modifications
    - Example is something like `deck = FrenchDeck(); deck[:3]`
    - It's also iterable!! `for card in deck` works!!
- If a `collection` has no `__contains__` method, the `in` operator does a *sequential scan*
    - So, if something is iterable, the sequential scan works! 
- __repr__ method is a built-in t oget the string representation of the object for inspection
    - If we didn't implement this in a class, a class instance would look weird when shown in console
    - Example: <Vector object at 0x10e100070>