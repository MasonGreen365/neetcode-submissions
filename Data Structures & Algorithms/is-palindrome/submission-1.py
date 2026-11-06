class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers to keep space : O(1)
        l, r = 0, len(s) - 1

        while l < r:
            #move two pointers to alpha numeric characters
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            #check palindrome crit.
            if s[l].lower() != s[r].lower():
                return False
            # move pointers inwards; step 1
            l, r = l + 1, r - 1
        return True 
    
    #alphaNum checks that char is inside allowed values for function
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')
        )

