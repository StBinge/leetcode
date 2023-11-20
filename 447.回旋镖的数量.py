#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#
from typing import List
# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        L=len(points)
        ret=0
        distances=[[0]*L for _ in range(L)]
        for i in range(L):            
            for j in range(i):
                dis=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                distances[i][j]=dis
                distances[j][i]=dis
        
        for i in range(L):
            cnt=1
            distances[i].sort()
            pre=0
            for d in distances[i][1:]:
                if d==pre:
                    cnt+=1
                else:
                    ret+=cnt*(cnt-1)
                    pre=d
                    cnt=1
            else:
                ret+=cnt*(cnt-1)
        return ret
                
# @lc code=end
points = [[0,0],[1,0],[2,0]]
assert Solution().numberOfBoomerangs(points)==2
points = [[1,1],[2,2],[3,3]]
assert Solution().numberOfBoomerangs(points)==2
points = [[1,1]]
assert Solution().numberOfBoomerangs(points)==0
