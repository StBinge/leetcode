#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#
from sbw import *
# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ret=len(intervals)
        r_max=0
        for s,e in intervals:
            if e<=r_max:
                ret-=1
            else:
                r_max=max(r_max,e)
        return ret

# @lc code=end

assert Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]])==2