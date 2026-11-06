#find longest substring from given string s
#substring criteria: cant contain duplicate characters

#hashmap gives us unique keys for every substring
#sliding window builds size substring

#o(n) runtime to iterate through array

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        #left pointer index
        l = 0
        res = 0

        for r in range(len(s)):
            #if dup character in set, remove left pointer from consideration
            while s[r] in charSet:
                charSet.remove(s[l])
                #shift left pointer
                l += 1
            #include r character in set for next consideration
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

                
        