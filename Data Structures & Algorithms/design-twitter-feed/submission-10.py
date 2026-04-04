class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followdict = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-1*self.time,tweetId])
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followers = self.followdict[userId] | {userId}
        for followeeId in followers:
            if followeeId in self.tweets:
                index=len(self.tweets[followeeId])-1
                time,tweetId = self.tweets[followeeId][-1]
                heap.append([time,tweetId,followeeId,index-1])
        heapq.heapify(heap)
        res = []
        while heap and len(res)<10:
            time,tweetId,followeeId,index=heapq.heappop(heap)
            res.append(tweetId)
            if index>=0:
                time,tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap,[time,tweetId,followeeId,index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followdict[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followdict[followerId]:
            self.followdict[followerId].remove(followeeId)
        
