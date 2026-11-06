# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        #hang onto the last node of previous group
        groupPrev = dummy   
        
        #do while loop just iterate through entire LL
        while True:
            #get first kth group
            kth = self.getKth(groupPrev, k)
            
            #break loop if we don't have any more
            if not kth:
                break
            groupNext = kth.next

            #reverse subgroup
            prev, curr = kth.next, groupPrev.next

            #simple reverse in place using prev, temp, curr
            #for subgroup only
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            #use temp to stitch together subgroup back to main
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    #getKth returns kth ListNode given 
    # - curr: current ListNode
    # - k: size of subgroup
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr