#we are working backwards; we want to see if fastest cars 
#collide with slowest cars; checking intersections. for faster cars 
#that reach target before solwer cars, we can say they are a fleet.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair, reverse=True):
            # intersection time for each car
            stack.append((target - p) / s)
            #check if collision occurs
            #must be at least two cars in stack for collision
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


        