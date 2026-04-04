class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1*wt for wt in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            y=heapq.heappop(heap) # first largest
            x=heapq.heappop(heap) # second largest
            
            y=-1*y
            x=-1*x
            
            if x<y:
                heapq.heappush(heap,-1*(y-x))
        return -1*heap[0] if len(heap)>0 else 0

        