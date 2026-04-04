class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        def get_freq_tuple(string):
            freq=[0]*26
            for s in string:
                freq[ord(s)-ord('a')]+=1
            return tuple(freq)

        for string in strs:
            freq_tup = get_freq_tuple(string)
            d[freq_tup].append(string)
        
        return list(d.values())

        