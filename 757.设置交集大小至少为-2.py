#
# @lc app=leetcode.cn id=757 lang=python3
#
# [757] 设置交集大小至少为2
#
from typing import List
# @lc code=start
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ans=0
        L=len(intervals)
        vals=[0]*L
        for i in range(L-1,-1,-1):
            j=intervals[i][0]
            for k in range(vals[i],2):
                ans+=1
                for p in range(i-1,-1,-1):
                    if intervals[p][1]<j:
                        break
                    vals[p]+=1
                j+=1
        return ans
# @lc code=end

intervals = [[1,3],[3,7],[8,9]]
assert Solution().intersectionSizeTwo(intervals)==5