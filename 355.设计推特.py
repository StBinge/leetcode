#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#
from typing import List
# @lc code=start
import heapq
class LinkNode:
    def __init__(self,val,next:'LinkNode') -> None:
        self.val=val
        self.next=next
class User:
    def __init__(self) -> None:
        self.news=[None]*10
        self.latest_id=-1
    
    def post_new(self,tweet_id,timestamp):
        self.latest_id+=1
        self.news[self.latest_id%10]=[timestamp,tweet_id]

    def get_news(self):
        ret=[]
        for i in range(10):
            nid=(self.latest_id-i)%10
            if not self.news[nid]:
                break
            ret.append(self.news[nid])
        return ret
class Twitter:

    def __init__(self):
        # self.follows=set()
        self.users:dict[int,User]={}
        self.timestamp=0
        self.follows:dict[int,set]={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        user=self.users.setdefault(userId,User())
        user.post_new(tweetId,self.timestamp)
        self.timestamp+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        users_id=list(self.follows[userId]) if userId in self.follows else []
        users_id.append(userId)
        posts=[]
        for uid in users_id:
            user=self.users.get(uid,None)
            if not user:
                continue
            # lastest_id=user.latest_id
            for new in user.get_news():
                # nid=(lastest_id-i)%10
                # new=user.news[nid]
                # if not new:
                #     break
                if len(posts)<10:
                    heapq.heappush(posts,(new[0],new[1]))
                    continue
                if new[0]<posts[0][0]:
                    break
                heapq.heappushpop(posts,(new[0],new[1]))
        ret=[]
        while posts:
            ret.append(heapq.heappop(posts)[1])
        return ret[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        follows=self.follows.setdefault(followerId,set())
        follows.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId==followerId:
            return
        if followerId not in self.follows:
            return

        self.follows[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

twitter = Twitter()
twitter.postTweet(1, 1)
print(twitter.getNewsFeed(1) )
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1) ) # 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
twitter.follow(1, 2)    # 用户 1 关注了用户 2
twitter.postTweet(2, 6) # 用户 2 发送了一个新推文 (推文 id = 6)
print(twitter.getNewsFeed(1) ) # 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
twitter.unfollow(1, 2)  # 用户 1 取消关注了用户 2
print(twitter.getNewsFeed(1))  # 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2