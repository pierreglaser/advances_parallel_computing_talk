>>> import pickle
>>> s = pickle.dumps([1, 2, 3])  # serialization (pickling) step
>>> s
b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
>>> depickled_list = pickle.loads(s)  # deserialization (unpickling) step
>>> depickled_list
[1, 2, 3]
