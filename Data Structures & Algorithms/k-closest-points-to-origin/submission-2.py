class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_from_origin = [[-1*(a**2+b**2),[a,b]] for a,b in points]
        heap=[]
        for dist in dist_from_origin:
            heapq.heappush(heap,dist)
            if len(heap)>k:
                heapq.heappop(heap)

        return [val[1] for val in heap]

        