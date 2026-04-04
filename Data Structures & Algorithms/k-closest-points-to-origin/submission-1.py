class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # no need to use math.sqrt since that would just add extra computation
        # since comparing distances if x1^2+y1^2 > x2^2+y2^2 =>  sqrt(x1^2+y1^2) > sqrt(x2^2+y2^2)
        # distance=[[(a**2+b**2),[a,b]] for a,b in points]
        # ### using min heap
        # heap=[]
        # res=[]
        # for dist in distance:
        #     heapq.heappush(heap,dist)
        #     if len(heap)>len(points)-k:
        #         val=heapq.heappop(heap)
        #         res.append(val[1])

        # return res

        ### using max heap
        distance=[[-1*(a**2+b**2),[a,b]] for a,b in points]
        heap=[]
        for dist in distance:
            heapq.heappush(heap,dist)
            if len(heap)>k:
                heapq.heappop(heap)

        return [val[1] for val in heap]
        