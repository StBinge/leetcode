#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#
from typing import List
# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:

        L=len(stones)
        for i in range(1,L):
            if stones[i]-stones[i-1]>i:
                return False
        dp=[set() for _ in range(L)]
        dp[0].add(0)
        for i in range(1,L):
            for j in range(i-1,-1,-1):
                dis=stones[j]-stones[i]
                if dis>j+1:
                    break
                if dis in dp[j] or dis-1 in dp[j] or dis+1 in dp[j]:
                    if i==L-1:
                        return True
                    dp[i].add(dis)
        return False
# @lc code=end
assert Solution().canCross([0,1,3,5,6,8,12,17])
assert Solution().canCross([0,1,2,3,4,8,9,11])==False
