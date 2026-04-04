class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[]
        for wt in stones:
            heapq.heappush(max_heap,-1*wt)

        while len(max_heap)>1:
            x=heapq.heappop(max_heap)
            y=heapq.heappop(max_heap)

            if x<y:
                new_wt=x-y
                heapq.heappush(max_heap,new_wt)

        return -1*max_heap[0] if len(max_heap)>0 else 0
        