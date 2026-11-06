#monotonic decreasing stack;
# top of stack represents lowest value, 
# when larger value seen, we pop temp (calculating difference and updating result)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #pair : [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        return result


        