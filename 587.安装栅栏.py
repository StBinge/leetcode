#
# @lc app=leetcode.cn id=587 lang=python3
#
# [587] 安装栅栏
#
from typing import List
# @lc code=start
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p,q,r):
            return (q[0]-p[0])*(r[1]-q[1])-(q[1]-p[1])*(r[0]-q[0])
        if len(trees)<4:
            return trees
        
        trees.sort()
        hull=[0]
        used=[False]*len(trees)
        for i in range(1,len(trees)):            
            while len(hull)>1 and cross(trees[hull[-2]],trees[hull[-1]],trees[i])<0:
                used[hull.pop()]=False
            hull.append(i)
            used[i]=True
        
        m=len(hull)
        for i in range(len(trees)-2,-1,-1):
            if used[i]:
                continue
            while len(hull)>m and cross(trees[hull[-2]],trees[hull[-1]],trees[i])<0:
                used[hull.pop()]=False
            hull.append(i)
            used[i]=True
        hull.pop()
        return [trees[i] for i in hull]       
        



# @lc code=end
assert Solution().outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]])==[[1,1],[2,0],[3,3],[2,4],[4,2]]
