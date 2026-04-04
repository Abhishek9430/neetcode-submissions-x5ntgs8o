class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            fl=[0]*26
            for char in s:
                fl[ord(char)-ord('a')]+=1 ## given only lower case chars
            
            d[tuple(fl)].append(s)
        return list(d.values())
