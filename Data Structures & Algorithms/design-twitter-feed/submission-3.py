class Twitter:

    def __init__(self):
        self.tweets=defaultdict(list)
        self.followers=defaultdict(set)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append([-1*self.time,tweetId])
        return
        
    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        followeeIds=self.followers[userId] | {userId} # consider followers + userId (set) all tweets
        heap=[]
        for fid in followeeIds:
            # i.e. if user has tweeted
            if fid in self.tweets:
                index = len(self.tweets[fid])-1 # last tweet index
                time_tweeted,tweet_id = self.tweets[fid][index]
                heap.append([time_tweeted,tweet_id,fid,index-1]) #next index

        heapq.heapify(heap)

        res=[]
        while heap and len(res)<10:
            # get the last tweet
            time,tweet_id,fid,index=heapq.heappop(heap)
            res.append(tweet_id)
            if index>=0:
                time_tweeted,tweet_id=self.tweets[fid][index]
                heapq.heappush(heap,[time_tweeted,tweet_id,fid,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        return
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        return
