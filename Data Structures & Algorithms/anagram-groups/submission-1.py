class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for idx,s in enumerate(strs):
            sorted_s=''.join(sorted(s))
            if sorted_s not in d:
                d[sorted_s]=[s]
            else:
                d[sorted_s].append(s)
        return list(d.values())
