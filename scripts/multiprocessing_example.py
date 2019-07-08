from multiprocessing import Process


def greet_friend(name):
    print(f"hello {name}!")


if __name__ == "__main__":
    p = Process(target=greet_friend, args=("Bob",))
    p.start()
    p.join()
