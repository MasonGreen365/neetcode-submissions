class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # charCount : list of anagrams
        for s in strs:
            count = [0] * 26 # create char array
            # use asci val to build counts
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())
