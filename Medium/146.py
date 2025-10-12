class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        node = Node(key, value)
        self.hashmap[key] = node
        self.insert(node)
        self.size += 1

        if self.size > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]
            self.size -= 1
