class TimeMap:

    def __init__(self):
        self.mr=defaultdict(list) # dict to store all timestamps
        self.kv=defaultdict(dict) # dict to store {key:{time:value}}
        
    def _search(self,nums,target):
        i=0
        j=len(nums)-1
        res=-1
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]<=target:
                res=mid
                i=mid+1
            else:
                j=mid-1
        return res

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key][timestamp]=value
        self.mr[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        timestamps=self.mr[key]
        if not timestamps:
            return ""
        idx=self._search(timestamps,timestamp)
        if idx==-1:
            return ""
        time=timestamps[idx]
        return self.kv[key].get(time,"")
        
