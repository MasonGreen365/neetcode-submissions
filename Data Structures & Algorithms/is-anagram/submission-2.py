#tried to use set; set is for having seen ONCE; dict would tell us exact # number of characters SEEN aka anagram.
# got confused about how to ACCESS dict, and in the event of no key found, return 0 .get(value, OPTIONAL return if not)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMap = {} # char : value
        for char in s:
            charMap[char] = charMap.get(char, 0) + 1
        for char in t:
            if charMap.get(char, 0) == 0:
                return False
            charMap[char] -= 1

        return True
        