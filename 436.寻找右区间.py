#
# @lc app=leetcode.cn id=436 lang=python3
#
# [436] 寻找右区间
#
from typing import List
# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N=len(intervals)
        starts,ends=list(zip(*intervals))
        starts=sorted([s,i] for i,s in enumerate(starts))
        ends=sorted([e,i] for i,e in enumerate(ends))
        ret=[-1]*N

        j=0
        for e,i in ends:
            while j<N and starts[j][0]<e:
                j+=1
            if j<N:
                ret[i]=starts[j][1]
        return ret
# @lc code=end
intervals = [[1,2]]
r=Solution().findRightInterval(intervals)
print(r)

intervals = [[3,4],[2,3],[1,2]]
r=Solution().findRightInterval(intervals)
print(r)

intervals = [[1,4],[2,3],[3,4]]
r=Solution().findRightInterval(intervals)
print(r)