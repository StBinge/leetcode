#
# @lc app=leetcode.cn id=1751 lang=python3
#
# [1751] 最多可以参加的会议数目 II
#
from sbw import *
# @lc code=start
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[1])
        N=len(events)
        f=[[0]*(k+1) for _ in range(N+1)]
        for i,(start,end,value) in enumerate(events):
            pre=bisect_left(events,start,key=lambda x:x[1],hi=i)
            for j in range(1,k+1):
                f[i+1][j]=max(f[i][j],f[pre][j-1]+value)
        return f[-1][-1]
# @lc code=end
assert Solution().maxValue(events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3)==9
assert Solution().maxValue(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2)==10
assert Solution().maxValue(events = [[1,2,4],[3,4,3],[2,3,1]], k = 2)==7
