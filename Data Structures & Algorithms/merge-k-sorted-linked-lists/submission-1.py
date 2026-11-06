# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
1. given list of sorted linked lists, merge K way. 
    - list of linked lists can be 0 (edge case)
    - linked lists can be 0 (edge case as well)
    - values can be negative 

2. approaches
    - iterative: o(n*m), space o(n) iterate through every node and check value, add to resultant list
    - min-heap: heapify each list, pop and add to resultant
    - sorted; how does that aid us?
    dynamic programming; merge adjacent lists in pairs and

"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #edge case handler
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        #to-do (easy part) (not really)
        #create dummy head
        dummy = ListNode()
        #grab ref to dummy head
        tail = dummy

        while l1 and l2:
            #grab lesser and append to tail
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            #move tail pointer once appended
            tail = tail.next

        #if after comparisons, append rest of lists
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


        