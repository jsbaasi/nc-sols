'''
map uid > set of tweets posted by them, elements being (time_added, tweet_id)
map uid > set of uids they're following
'''
class Twitter:
    def __init__(self):
        self.user_tweets = defaultdict(set)
        self.users_followed = defaultdict(set)
        self.step = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].add((self.step, tweetId))
        self.step+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.user_tweets
        followed = self.users_followed[userId]
        all_tweets = tweets[userId].union(
            *(tweets[fid] for fid in followed)
        )
        return [tweet_id for time_added, tweet_id in heapq.nlargest(10, all_tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users_followed[followerId].discard(followeeId)