#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#
from sbw import *
# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ret=0
        mod=[0]*60
        for t in time:
            m=t%60
            rm=60-m
            if rm==60:
                rm=0
            ret+=mod[rm]
            mod[m]+=1
        return ret
# @lc code=end
time = [60,60,60]
assert Solution().numPairsDivisibleBy60(time)==3

time = [30,20,150,100,40]
assert Solution().numPairsDivisibleBy60(time)==3
