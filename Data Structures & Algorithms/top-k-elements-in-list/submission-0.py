# k most frequent elements
# HashMap with frequencies 
# up to n frequencies:
# index is frequency
# val is list of nums at that freq.

# alt. is using max heap...? 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build bucketsort data structure
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # build counts, handle no val existing
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # update freqency buckets
        for num, count in count.items():
            freq[count].append(num)
        
        # create K result list
        res = []
        #from end of freq, work backwards
        #empty [] values in potentially some freq[i], 
        # .append doesn't add anything (None)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
            #stop when res is K deep
            if len(res) == k:
                return res



        
        