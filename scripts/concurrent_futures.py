>>> from concurrent.futures import ProcessPoolExecutor
>>> executor = ProcessPoolExecutor(max_workers=2)
>>> def greet_friend(name):
...     return "hello {}!".format(name)
...
>>> results = executor.map(greet_friend, ("Alice", "Bob"))  # non-blocking
>>> for r in results:  # blocking until the next task completes.
...     print(r)
