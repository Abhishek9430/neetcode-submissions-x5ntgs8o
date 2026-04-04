class Twitter:

    def __init__(self):
        self.followers=defaultdict(set)
        self.tweets=defaultdict(list)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append([-1*self.time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followers=self.followers[userId] | { userId } # userid + followerid
        heap=[]
        for followeeId in followers:
            if followeeId in self.tweets:
                index=len(self.tweets[followeeId])-1
                time,tweetId=self.tweets[followeeId][index]
                heap.append([time,tweetId,followeeId,index-1])
        heapq.heapify(heap)
        res=[]
        while heap and len(res)<10:
            time,tweetId,followeeId,index=heapq.heappop(heap)
            res.append(tweetId)
            if index>=0:
                time,tweetId=self.tweets[followeeId][index]
                heapq.heappush(heap,[time,tweetId,followeeId,index-1]) 
        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
