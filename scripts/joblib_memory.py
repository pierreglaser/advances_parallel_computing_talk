>>> @memory.cache
... def f(x):
...     print('Running f(%s)' % x)
...     return x
>>> print(f(1))  # computes f(1), dumps the result to disk
Running f(1)
1
>>> print(f(1))  # does not re-run f, simply grabs the result from the disk
1
