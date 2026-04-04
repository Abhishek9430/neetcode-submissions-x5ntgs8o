class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for char in strs:
            freq_arr = [0]*26
            for c in char:
                freq_arr[ord(c)-ord("a")]+=1
            d[tuple(freq_arr)].append(char)
        
        return list(d.values())
            

        