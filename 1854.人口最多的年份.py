#
# @lc app=leetcode.cn id=1854 lang=python3
#
# [1854] 人口最多的年份
#
from sbw import *
# @lc code=start
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dif=[0]*101
        for bir,de in logs:
            dif[bir-1950]+=1
            dif[de-1950]-=1
        
        ret=0
        Mx=0
        cnt=0
        for i,v in enumerate(dif):
            cnt+=v
            if cnt>Mx:
                Mx=cnt
                ret=i+1950
        return ret
# @lc code=end
assert Solution().maximumPopulation([[1950,1961],[1960,1971],[1970,1981]])==1960
assert Solution().maximumPopulation([[1993,1999],[2000,2010]])==1993
