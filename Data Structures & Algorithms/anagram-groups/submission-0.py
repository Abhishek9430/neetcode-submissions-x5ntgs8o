class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        res=[]
        for idx,s in enumerate(strs):
            sorted_s=''.join(sorted(list(s)))
            if sorted_s not in d:
                d[sorted_s]=[s]
            else:
                d[sorted_s].append(s)
        return list(d.values())
