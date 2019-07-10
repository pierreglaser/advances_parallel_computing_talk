>>> import pickle
>>> import cloudpickle
>>> pickle.dumps(lambda x: x + 1)  # would cause arbitrary code execution
