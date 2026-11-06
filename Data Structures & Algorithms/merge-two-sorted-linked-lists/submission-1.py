# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
runtime: O(n)
space: O(n)

iterate through 1 & 2
conditional add to merged list
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        #while BOTH lists exists
        while list1 and list2:
            if list1.val < list2.val:
                #set dummy pointer to list1 to capture
                node.next = list1
                #increment
                list1 = list1.next
            else:
                #set dummy pointer to list2 to capture
                node.next = list2
                #inrecement
                list2 = list2.next
            #increment dummy & repeat
            node = node.next
        #set remainder of either list to next after while loop
        node.next = list1 or list2
        return dummy.next
