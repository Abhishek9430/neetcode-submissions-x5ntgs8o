class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followdict = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time,tweetId])
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followings = self.followdict[userId] | {userId}
        tweets = []
        for follow in followings:
            tweet = self.tweets[follow]
            tweets.extend(tweet)
        tweets.sort(reverse=True)
        res = []
        if len(tweets)>10:
            for i in range(10):
                res.append(tweets[i][1])
            return res
        else:
            return [t[1] for t in tweets]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followdict[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followdict[followerId]:
            self.followdict[followerId].remove(followeeId)
        
