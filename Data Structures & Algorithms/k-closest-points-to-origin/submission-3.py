class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_array = [[-1*(a**2+b**2),[a,b]] for a,b in points]
        heap = []

        for distance in dist_array:
            heapq.heappush(heap,distance)
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [dist[1] for dist in heap]
