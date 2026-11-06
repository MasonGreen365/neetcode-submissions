"""
1. s (ONLY uppercase characters) and int K to choose k chars to replace with any other character. find longest substring
- edge cases: s will be at least 1 char, k can be 0
- in case of tie (AAABBB), k 1; result will be the same

2. sliding window; start at left; check for max using current character and decrementing k. grow to max. 
- move left pointer once? checking substring
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l = 0
        # res = 0

        # for r in range(len(s) - 1):
        #     char = s[l]
        #     temp = 0
        #     while s[r] == char:
        #         temp += 1
        #         while k > 0 and k <= len(s):
        #             temp += 1
        #             k -= 1
        #     l = r - k
        #     res = max(temp, res)
        # return res
        
        count = {} # hash map char : frequency
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
            


        