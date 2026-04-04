class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        
        heap=[]
        for key,value in d.items():
            heapq.heappush(heap,[value,key])
            if len(heap)>k:
                heapq.heappop(heap)
        return [val[1] for val in heap]
