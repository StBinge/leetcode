#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#
from typing import List
# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        cnt=0

        for i in range(1,len(timeSeries)):
            cnt+=min(duration,timeSeries[i]-timeSeries[i-1])
        return cnt+duration

# @lc code=end

assert Solution().findPoisonedDuration([1,4],2)==4
assert Solution().findPoisonedDuration([1,2],2)==3