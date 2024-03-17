#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#
from sbw import *
# @lc code=start
import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        L=len(startTime)
        jobs=sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
        f=[0]*(L+1)
        for i in range(L):
            start=jobs[i][0]
            j=bisect.bisect_right(jobs,start,key=lambda j:j[1],hi=i+1)
            f[i+1]=max(f[i],f[j]+jobs[i][2])
        return f[-1]
# @lc code=end
assert Solution().jobScheduling([6,15,7,11,1,3,16,2],[19,18,19,16,10,8,19,8],[2,9,1,19,5,7,3,19])==41
assert Solution().jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4])==6
assert Solution().jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60])==150
assert Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])==120
