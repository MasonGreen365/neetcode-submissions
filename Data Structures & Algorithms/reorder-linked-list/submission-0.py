# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # # capture head
        # prev = head
        # #modify next value
        # curr = head.next
        # #use stack to reverse order
        # tempStack = []
        # #until end of list, enter into stack
        # while curr.next:
        #     tempStack.append(curr)
        #     curr = curr.next
        # while tempStack:
        #     prev.next = curr
        #     curr = tempStack.pop()
        # i assumed incorrect order of operations and also got it wrong

        #o(n) + o(1) We want to avoid extra memory

        #fast and slow pointers get us midpoint; slow reaches mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #take second portion of list, reverse next pointers
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge two portions together
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2


            
            

        