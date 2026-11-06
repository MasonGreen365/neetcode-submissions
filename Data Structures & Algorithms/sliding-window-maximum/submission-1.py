"""
1. find maximum in window for n window (sized k) positions given array
    return List of maximum values per
2. approaches:
    - brute force. for every unique window combination, find max and append
    - max-heap + sliding window. for pop l and append new r and iterate through

3. edge cases:
    - k can be == or < nums.length, meaning at least 1 window position possible
    - we can have negative numbers, so witha. max heap do we need to watch out for that?

            [1 2 1 0 4 2 6]
window       l - r
heap(max)    1 2 2 2 4 4 6
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [] # heap programming takes effect using heapq.functions
        output = []
        #for all numbers
        for i in range(len(nums)):
            #multilpy by -1 for max heap
            heapq.heappush(heap, (-nums[i], i))
            # once window becomes side k, slide
            if i >= k- 1:
                #pop elements that are outside window
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                #append max value for given window
                output.append(-heap[0][0])
        return output





                

            
        