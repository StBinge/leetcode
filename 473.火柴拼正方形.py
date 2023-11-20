#
# @lc app=leetcode.cn id=473 lang=python3
#
# [473] 火柴拼正方形
#
from typing import List
# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # cnt={}
        # S=0
        # for s in matchsticks:
        #     c=cnt.get(s,0)+1
        #     cnt[s]=c
        #     S+=s
        S=sum(matchsticks)
        if S%4:
            return False
        # matchsticks.sort(reverse=True)
        edge=S//4
        L=len(matchsticks)
        total=(1<<L)
        dp=[-1]*total
        dp[0]=0
        for s in range(1,total):
            for k,v in enumerate(matchsticks):
                bit=1<<k
                if s & bit ==0:
                    continue
                s1=s & ~bit
                if dp[s1]>=0 and dp[s1]+v<=edge:
                    dp[s]=(dp[s1]+v)%edge
        return dp[-1]==0

# @lc code=end

assert Solution().makesquare([13,11,1,8,6,7,8,8,6,7,8,9,8])
assert Solution().makesquare([10,6,5,5,5,3,3,3,2,2,2,2])
assert Solution().makesquare([1,1,2,2,2])
assert Solution().makesquare([3,3,3,3,4])==False