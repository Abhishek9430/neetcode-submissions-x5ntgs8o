class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q=deque()

        freq={}
        for t in tasks:
            freq[t]=freq.get(t,0)+1
        
        maxheap=[]
        for val in freq.values():
            heapq.heappush(maxheap,-1*val)

        time=0
        while maxheap or q:
            time+=1
            if maxheap:
                task=abs(heapq.heappop(maxheap))
                rem_tasks=task-1
                if rem_tasks>0:
                    q.append((-1*rem_tasks,time+n))
            if q and q[0][1]==time: # i.e. the very first element(as per time) in q have attained time equal to cooling time
                cooled_task=q.popleft()
                cooled_task=cooled_task[0]
                heapq.heappush(maxheap,cooled_task)
        return time
        