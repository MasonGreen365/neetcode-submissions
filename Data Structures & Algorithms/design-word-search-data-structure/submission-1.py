class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                # add c to d
                d[c] = {}
            #traverse into new empty dict.
            d = d[c]
        #use null byte to punctuate word
        d['\x00'] = '\x00'
        

    # because . is in place for char wherever and will work, we must
    # try all paths. must find at least 1 true path that terminates
    def search(self, word: str) -> bool:
        def dfs(curr, idx):
            #did we find complete word (terminated by special char)
            if idx == len(word):
                return bool('\x00' in curr)
            #no? grab char
            letter = word[idx]
            #if char
            if letter != '.':
                #is letter in curr dict?
                if letter not in curr: return False
                #recursive call if dict exists
                else: return dfs(curr[letter], idx+1)
            #if '.', try all options except where '\x00' terminates path
            else:
                return any(dfs(curr[letter], idx+1) for letter in curr if letter != '\x00')


        return dfs(self.trie, 0)
