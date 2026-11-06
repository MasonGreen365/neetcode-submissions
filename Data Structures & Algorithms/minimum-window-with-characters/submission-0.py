"""
1. find shortest substring of s that includes every char of t in it 
    - include duplicates of char from t
    - if substring doesnt exist, return ""

2. sliding window
    - only initialize window l pointer where s[l] is in hashmap
    t 
    - from there, grow r to attempt to capture rest of characters
    - if l value found again, check length of that substring against current and update window

how to move l pointer to r? 
        [O U Z O D Y X A Z V]
         - - l - - r
         - - l - - 1 r          substring found, r != len(s)
         - - 1 - - l 1 r - -
         - - 1 - - l 1 - r -    substring found, shorter

mark where char occurs, possible bounds for l. 
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t): return ""

        countT, window = {}, {}

        for c in t:
            # build map for T
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update result
                #if size of new window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        #grab sliding window bounds
        l, r  = res
        #return substring ONLY if resLen has been updated
        return s[l:r+1] if resLen != float("infinity") else ""


        
        