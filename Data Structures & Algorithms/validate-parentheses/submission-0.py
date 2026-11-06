class Solution:
    def isValid(self, s: str) -> bool:
        #create stack (python list)
        stack = []
        #create hashMap check
        checkMap = {"]" : "[", "}" : "{", ")" : "("}
        for c in s:
            if c in checkMap:
                # if stack is not empty and char matches bracket
                if stack and stack[-1] == checkMap[c]:
                    stack.pop()
                else:
                    return False
            else: stack.append(c)
        return not stack
