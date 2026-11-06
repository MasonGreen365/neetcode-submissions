# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next

        
        removeIndex = size - n
        # if size <= 1:
        #     return []
        if removeIndex == 0:
            return head.next

        temp = head
        for i in range(size - 1):
            if (i+1) == removeIndex:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head




        