"""
I am confused on sliding window algo
we create sliding window of len(s1), but shift under what conditions?
My idea was to use a hashmap and remove matched characters, then return true if the size was 0. However, it doesn't make sense to do this given a sliding window approach. if we simply shift over our l r pointers, we check twice for certain characters. watching video now.

i misunderstood the video; permutation is substring matched where we want same length substring that is permutation/anagram of our s1. so thats why using a sliding window is opitmal. 

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0 
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
        # # build 1 hash sets for s1 string o(n)
        # # sliding window to check if exists inside? if doesnt
        # #shift l r to the right of size s1

        # #build check map
        # charMap = {} # char : freq
        # for c in s1:
        #     charMap[c] = 1 + charMap.get(c, 0)
      
        # #sliding window
        # #slide if doesn't contain char
        # #expand if not ? confused 
        # l = 0
        # for r in range(len(s2) - 1):
        #     #objective; remove chars from dict and if 0
        #     #permutation exits
        #     if s[r] in charMap && charMap[s[r]] == 1:
        #         charMap.pop(s[r])
        #     elif s[r] in charMap:
        #         charMap[s[r]] -= 1
        # return True if len(charMap) == 0           

        