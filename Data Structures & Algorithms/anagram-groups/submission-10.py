class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        def get_freq(word):
            res = [0]*26
            for char in word:
                res[ord(char)-ord('a')]+=1
            return tuple(res)
        
        for word in strs:
            tup = get_freq(word)
            d[tup].append(word)
        
        return list(d.values())
        