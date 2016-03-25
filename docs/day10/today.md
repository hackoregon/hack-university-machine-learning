# Today

## Doctests

Copy and paste and example from the ipython console into your docstring (triple-quoted string at the top of a function, class or module)

```python
"""Example doctests

Save this in a file called "module_containing_doctests.py"
"""

>>> function()
42
"""

def function(x=None):
    """Docstring describing what the function does

    This function always returns the right answer!

    >>> function(9)
    42
    """
    return 42
```

Then to run that test just...

```python
>>> import doctest
>>> import module.containing.doctests
>>> doctest.testmod(module_containing_doctests)
```