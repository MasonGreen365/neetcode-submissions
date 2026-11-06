"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 

        #build dict for each node, and optional null node
        oldToCopy = {None : None}

        #clone linked list nodes
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next= oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]

        #get size of list
        # size = 0
        # temp = head
        # #bulid array of rand references
        # randomRef = []
        # while temp:
        #     size += 1
        #     temp = temp.next
        #     randomRef.append(temp.random)
        
        # #iterate through list, create deep copy
        # #how to get random without iterating through another N times

        # #EDGE CASE: points to null at end of array if random empty
        # #create deep copy of only head
        # temp = head
        # newHead = Node(head.val, None, head.random)
        # for i, val in enumerate(randomRef):
        #     curr = newHead
        #     while temp:
        #         curr.next = temp.next.copy()
        #         temp = temp.next





        
        