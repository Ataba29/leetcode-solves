from collections import defaultdict
from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.k = 10
        self.follows = defaultdict(set)  # follower -> set of followees
        self.tweets = defaultdict(list)  # user -> list of (timestamp, tweetId)
        self.t = 0  # global timestamp to order tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        # store negative timestamp so larger negative = newer tweet
        self.tweets[userId].append((-self.t, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followed = list(self.follows[userId]) + [userId]
        all_tweets = []

        # collect all tweets from the user and followees
        for follow in followed:
            all_tweets.extend(self.tweets[follow])

        # get k most recent tweets (largest negative timestamps)
        most_recent = heapq.nsmallest(self.k, all_tweets)
        # return only tweet IDs, newest first
        return [tweet for _, tweet in sorted(most_recent)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
