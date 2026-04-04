class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[[math.sqrt(a**2+b**2),[a,b]] for a,b in points]

        heap=[]
        res=[]
        for dist in distance:
            heapq.heappush(heap,dist)
            if len(heap)>len(points)-k:
                val=heapq.heappop(heap)
                res.append(val[1])

        return res
        