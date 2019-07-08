>>> from loky import ProcessPoolExecutor
>>> executor = ProcessPoolExecutor(max_workers=2)
>>> def greet_friend(name):
...     return "hello {}!".format(name)
...
>>> for result in executor.map(greet_friend, ("Alice", "Bob")):
...     print(result)
