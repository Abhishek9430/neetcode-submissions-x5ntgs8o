class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        for n in nums:
            freq_dict[n]=freq_dict.get(n,0)+1
        
        arr=[]
        for val,freq in freq_dict.items():
            arr.append([freq,val])

        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res