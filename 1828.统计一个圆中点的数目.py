#
# @lc app=leetcode.cn id=1828 lang=python3
#
# [1828] 统计一个圆中点的数目
#
from sbw import *
# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ret=[]
        for cx,cy,r in queries:
            r2=r*r
            cnt=0
            for x,y in points:
                d=(cx-x)**2+(cy-y)**2
                cnt+=d<=r2
            ret.append(cnt)
        return ret
# @lc code=end
assert Solution().countPoints(points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]])==[2,3,2,4]
assert Solution().countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]])==[3,2,2]
