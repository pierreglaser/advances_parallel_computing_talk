from multiprocessing import Pool


def greet_friend(name):
    print('hello {}!'.format(name))


if __name__ == "__main__":
    p = Pool(3)
    results = p.map(greet_friend, ["Bob", "Alice", "Paul"])
