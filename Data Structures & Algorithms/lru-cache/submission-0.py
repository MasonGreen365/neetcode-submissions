# smells like fast/slow pointers where we cycle through and either update or replace depending on critera

# get or put considers being used so its not cycle, might be heap?
"""
how do linked lists help us here?
natruallly, head is the first obj put in. 
size declares size of linked list
do we move things around coresponding to most used?
we want to do things in o(1) time
hashmap is best
hashmap val is pointer to LL
hashmap pointer lookup gives o(1)
pointers point to least used and most recent
"""
#helper doubly linked Node class
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        #dummy nodes for LRU and most recent
        self.left, self.right = Node(0,0), Node(0,0)
        #point to eachother for doubly linked
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            #access node value through cache ! (not value directly)
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove from list and delete LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
