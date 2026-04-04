class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        ### initialise linked list with dummy endnodes
        self.right=Node(0,0)
        self.left=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        
    def insert_node(self,node):
        prev=self.right.prev
        nxt=self.right
        prev.next=node
        node.prev=prev
        node.next=nxt
        nxt.prev=node

    def remove_node(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert_node(self.cache[key])

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]
        
