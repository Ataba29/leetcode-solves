class MyHashMap:

    def __init__(self):
        self.n = 10**6 + 1
        self.arr = [-1] * self.n

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = -1

