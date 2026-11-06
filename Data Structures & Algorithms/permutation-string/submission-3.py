"""
I am confused on sliding window algo
we create sliding window of len(s1), but shift under what conditions?
My idea was to use a hashmap and remove matched characters, then return true if the size was 0. However, it doesn't make sense to do this given a sliding window approach. if we simply shift over our l r pointers, we check twice for certain characters. watching video now.

i misunderstood the video; permutation is substring matched where we want same length substring that is permutation/anagram of our s1. so thats why using a sliding window is opitmal. 

"""
from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        expected = Counter(s1)

        l = 0
        actual = defaultdict(int)
        print(actual.items(), expected)

        for r in range(len(s2)):
            # add right char of window to actual
            actual[s2[r]] += 1
            # print(f"comparing {r, s2[r]} against expected values")
            while actual[s2[r]] > expected[s2[r]]:
                # print(f" actual: {actual[s2[r]]} > expected {expected[s2[r]]}")
                actual[s2[l]] -= 1
                l += 1

            # print(actual.items(), expected)
            # print(f"l: {l}, r: {s2[r]}")
            if (r - l + 1) == len(s1):
                return True
        return False
  


        