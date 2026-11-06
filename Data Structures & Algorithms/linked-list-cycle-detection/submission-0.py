# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. problem: return true if cycle is inside linked list, where one node can be visited again using next pointer
- what does index give us? tells us index at begining of cycle
- tail node will have next pointer pointed at index-th node, startign cycle. 
- index = -1 where tail points to null; no cycle exists
- we create index ?
2. examples shown better demonsrtate problem.
3. while loop. loop until -1 .next. infinite loop breaks this.
    hashmap. add vals keyed at index to hashmap. exit if -1. end once revisited.
    EDGE CASE:
        null input; .next = null; return true
        empty input; .next = null; return true
        index = out of bounds in linked list; ?

4. write hashmap pseudo code
"""
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         #declare hashmap
#         checkmap = []
#         #check if null/empty , return true
#         if head.next == None or head == None:
#             return False;
#         #while .next exists
#         while head.next:
#             #check for -1 index val
#             if head.next == -1:
#                 return True;
#             #hashmap.add[val;index]
#             checkmap.add(head.val)
#             #head = head.next
#             head = head.next
#         return False;

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #declare SET (not hashmap)
        #seen = {}
        seen = set()
        current = head
        #enter loop if val exists:
        while current:
            if current in seen:
                return True
                #cycle exists
            seen.add(current)
            #step forward
            current = current.next
        return False




        