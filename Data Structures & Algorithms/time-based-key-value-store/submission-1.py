class TimeMap:

    def __init__(self):
        self.map = {} # { k : [(timestamp, value)...]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        #edge case: Key not in map
        if key not in self.map: return ""
        
        lst  =  self.map[key]

        #edge case: timestamp is less than whats available
        if timestamp < lst[0][0]: return ""

        #search for nearest timestamp
        n = len(lst)
        l, r = 0, n - 1
        while l < r:
            m = (l+r+1) // 2 #critical step; we want m to be r pointer
            m_timestamp = lst[m][0]
            if m_timestamp > timestamp:
                r = m - 1
            elif m_timestamp < timestamp:
                l = m
            else:
                return lst[m][1]
        return lst[l][1]
        
