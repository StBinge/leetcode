#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
from typing import List
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        cnt=1
        right=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=right:
                cnt+=1
                right=intervals[i][1]
        return len(intervals)-cnt
# @lc code=end
assert Solution().eraseOverlapIntervals([ [1,2], [1,2], [1,2] ])==2
assert Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])==1
assert Solution().eraseOverlapIntervals([ [1,2], [2,3] ])==0
