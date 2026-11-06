#i assumed that I could use '#' as a delimiter for separating our strings
# code says we can use ANY of 256 ASCII values, so that doesn't work.

#instead, we can patternmatch by creating key of digits representing every string lengt.
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))) # "int length of string"
            res.append("#") #delimiter
            res.append(s)
        return "".join(res) #iterating over res, join by ""

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #what position we are at in input string
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res