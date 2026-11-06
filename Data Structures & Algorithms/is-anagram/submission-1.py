class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # init check
        if len(s) != len(t):
            return False

        # create hashmaps
        countS, countT = {}, {}

        #build hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # check values
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

        