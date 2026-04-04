class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for word in strs:
            fl=[0]*26
            for char in word:
                ordc=ord('a')-ord(char)
                fl[ordc]+=1
            d[tuple(fl)].append(word)
        return list(d.values())
        