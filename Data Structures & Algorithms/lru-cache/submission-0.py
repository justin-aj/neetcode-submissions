class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.left = Node(0, 0)   # LRU dummy
        self.right = Node(0, 0)  # MRU dummy
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # insert at MRU end (just before right dummy)
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)  # move to MRU end
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key, value)
        self.hashmap[key] = node
        self.insert(node)
        if len(self.hashmap) > self.capacity:
            # evict LRU (node after left dummy)
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]