class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}

        self.right=Node(0,0)
        self.left=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove the node first and add it at end of list to make
            # it most recently used
            self.removeNode(self.cache[key])
            self.addNode(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        new_node=Node(key,value)
        if key in self.cache:
            # remove node first and then add
            self.removeNode(self.cache[key])

        self.addNode(new_node)
        self.cache[key]=new_node
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.removeNode(lru)
            del self.cache[lru.key]

    def addNode(self,node):
        prev=self.right.prev
        nxt=self.right
        prev.next=node
        node.prev=prev
        node.next=nxt
        nxt.prev=node

    def removeNode(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        
