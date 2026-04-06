class Node:
    def __init__(self,key = 0,value = 0):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = {}
        self.right = Node()
        self.left = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def add(self,node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    
    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next =  next
        next.prev = prev

    def get(self, key: int) -> int:

        # if key exists in lru then remove node
        if key in self.lru:
            node = self.lru[key]
            self.remove(node)
            self.add(node)
            return self.lru[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key,value)
        if key in self.lru:
            self.remove(self.lru[key])

        self.add(node)
        self.lru[key]=node
        if len(self.lru) > self.cap:
            # lru is the right most node
            lru_node = self.left.next

            # remove lru
            self.remove(lru_node)

            # remove from cache
            del self.lru[lru_node.key]
        
        
