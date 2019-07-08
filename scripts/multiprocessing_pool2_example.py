import os
import time
import multiprocessing as mp
from multiprocessing import Pool
# from concurrent.futures import ProcessPoolExecutor
from loky import ProcessPoolExecutor


def greet_friend(name):
    print(os.getpid())
    time.sleep(5)


class A:
    def __reduce__(self):
        pass

if __name__ == "__main__":
    p = Pool(3)
    # p = ProcessPoolExecutor(max_workers=3)
    results = p.map(greet_friend, ["Bob", "Alice", "Paul"])
    for r in results:
        print(r)
