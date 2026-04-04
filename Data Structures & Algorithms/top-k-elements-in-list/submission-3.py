from heapq import heapify,heappop,heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        for n in nums:
            freq_dict[n]=freq_dict.get(n,0)+1

        heap=[]
        heapify(heap)
        for key,value in freq_dict.items():
            heappush(heap,(value,key))

        for i in range(len(heap)-k):
            heappop(heap)

        res=[]
        # print(heap)
        for i in range(len(heap)):
            res.append(heappop(heap)[1])
        return res