#
# @lc app=leetcode.cn id=1348 lang=python3
#
# [1348] 推文计数
#
from sbw import *
# @lc code=start
from sortedcontainers import SortedDict
class TweetCounts:

    def __init__(self):
        self.memo:dict[str,SortedDict]={}

    def recordTweet(self, tweetName: str, time: int) -> None:
        times=self.memo.setdefault(tweetName,SortedDict())
        times[time]=times.get(time,0)+1


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        gap=60
        if freq=='hour':
            gap=3600
        elif freq=='day':
            gap=86400
        # ret=[]
        times=self.memo[tweetName]
        keys=list(times.keys())
        ret=[0]*((endTime-startTime)//gap+1)
        idx=bisect_left(keys,startTime)
        for t in keys[idx:]:
            if t>endTime:
                break
            j=(t-startTime)//gap
            ret[j]+=times[t]
        return ret


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
# @lc code=end
tweetCnt=TweetCounts()
tweetCnt.recordTweet('tweet0',857105800)
tweetCnt.recordTweet('tweet1',255428777)
tweetCnt.recordTweet('tweet2',13881700)
tweetCnt.recordTweet('tweet3',82366032)
tweetCnt.recordTweet('tweet4',334311127)
assert tweetCnt.getTweetCountsPerFrequency("minute", "tweet0", 255428777,255438544)==[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
assert tweetCnt.getTweetCountsPerFrequency("day", "tweet2", 857105800,857108372)==[0]
assert tweetCnt.getTweetCountsPerFrequency("minute", "tweet4", 334311127,334316350)==[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
assert tweetCnt.getTweetCountsPerFrequency("hour", "tweet3", 82366032,82370980)==[1,0]

tweetCnt=TweetCounts()
tweetCnt.recordTweet('tweet0',13)
tweetCnt.recordTweet('tweet1',16)
tweetCnt.recordTweet('tweet2',12)
tweetCnt.recordTweet('tweet3',18)
tweetCnt.recordTweet('tweet4',82)
tweetCnt.recordTweet('tweet3',89)
assert tweetCnt.getTweetCountsPerFrequency("day", "tweet0", 89,9471)==[0]
assert tweetCnt.getTweetCountsPerFrequency("hour", "tweet3", 13,4024)==[2,0]


tweetCnt=TweetCounts()
tweetCnt.recordTweet('tweet3',0)
tweetCnt.recordTweet('tweet3',60)
tweetCnt.recordTweet('tweet3',10)
assert tweetCnt.getTweetCountsPerFrequency("minute", "tweet3", 0, 59)==[2]
assert tweetCnt.getTweetCountsPerFrequency("minute", "tweet3", 0, 60)==[2,1]
tweetCnt.recordTweet('tweet3',120)

assert tweetCnt.getTweetCountsPerFrequency("hour", "tweet3", 0, 210)==[4]
