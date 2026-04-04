class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for task in tasks:
            d[task]=d.get(task,0)+1

        q=deque()
        heap=[]
        for task_freq in d.values():
            heapq.heappush(heap,-1*task_freq)

        time=0
        while q or heap:
            time+=1
            if heap:
                task=abs(heapq.heappop(heap))
                rem_task=task-1
                if rem_task>0:
                    q.append([-1*rem_task,time+n])
            if q and q[0][1]==time:
                cooled_task=q.popleft()
                cooled_task=cooled_task[0]
                heapq.heappush(heap,cooled_task)
        return time
                

            
            
        