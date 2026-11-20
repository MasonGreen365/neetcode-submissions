import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        #max heap variant; working with negatives
        maxHeap = [-val for val in counts.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque() # pairs of [-count, time available]

        while maxHeap or q:
            time += 1
            if maxHeap:
                #decrement largest val
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
                


        