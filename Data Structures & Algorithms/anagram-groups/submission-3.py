class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            ref=list(word)
            ref.sort()
            ref=tuple(ref)
            if ref in d:
                d[ref].append(word)
            else:
                d[ref]=[word]
        return list(d.values())
        