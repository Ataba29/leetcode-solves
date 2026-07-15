class MyHashSet:

    def __init__(self):
        self.n = 10**6 + 1
        self.arr = [False] * self.n

    def add(self, key: int) -> None:
        self.arr[key] = True

    def remove(self, key: int) -> None:
        self.arr[key] = False

    def contains(self, key: int) -> bool:
        return self.arr[key]
