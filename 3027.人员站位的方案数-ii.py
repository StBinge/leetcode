#
# @lc app=leetcode.cn id=3027 lang=python3
#
# [3027] 人员站位的方案数 II
#
from sbw import *
# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:[x[0],-x[1]])
        ret=0
        L=len(points)
        for i in range(L):
            _,y1=points[i]
            ma=float('-inf')
            for j in range(i+1,L):
                _,y2=points[j]
                if ma<y2<=y1:
                    ret+=1
                    ma=y2
        return ret
# @lc code=end
assert Solution().numberOfPairs([[3,2],[3,6]])==1
assert Solution().numberOfPairs(points = [[3,1],[1,3],[1,1]])==2
assert Solution().numberOfPairs([[6,2],[4,4],[2,6]])==2
assert Solution().numberOfPairs([[1,1],[2,2],[3,3]])==0
