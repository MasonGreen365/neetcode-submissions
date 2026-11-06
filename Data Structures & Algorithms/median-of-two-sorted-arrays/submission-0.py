"""
1. given two sorted arrays, find median value amongst all elements

2. brute force: merge two sorted arrays; then find middle (O(m + n))
Binary Search: create conditional cut for first array, where median is edge of cut on left half, and edge on right
    - left side contains exactly half (or half + 1) and all are <= elemetns on right side


"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # swap if sizes are mismatched
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        lo, hi = 0, m
        #BS for nums1 to find cut mark
        while lo <= hi:
            #partition for nums1
            i = (lo + hi) // 2
            #partition for nums2 (remaining values to derive median)
            j = (m + n + 1) // 2 - i

            #define boundary edges for cut
            #edge cases values are not available; use +/- inf
            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            #check if we found boundary
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2) 
                return ((max(left1, left2) + min(right1, right2)) / 2)
            elif left1 > right2:
                hi = i - 1
            else: 
                lo = i + 1


        