class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for ele in nums:
            freq[ele] = freq.get(ele,0)+1

        heap=[]
        for key,val in freq.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [item[1] for item in heap]
        