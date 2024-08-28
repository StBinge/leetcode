#
# @lc app=leetcode.cn id=1591 lang=python3
#
# [1591] 奇怪的打印机 II
#
from sbw import *
# @lc code=start
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        R,C=len(targetGrid),len(targetGrid[0])
        up=[60]*61
        down=[0]*61
        left=[60]*61
        right=[0]*61
        colors=set()
        for r in range(R):
            for c in range(C):
                color=targetGrid[r][c]
                colors.add(color)
                up[color]=min(up[color],r)
                down[color]=max(down[color],r)
                left[color]=min(left[color],c)
                right[color]=max(right[color],c)
        graph=[[False]*61 for _ in range(61)]
        indeg=[0]*61
        for out_color in colors:
            for r in range(up[out_color],down[out_color]+1):
                for c in range(left[out_color],right[out_color]+1):
                    inner_color=targetGrid[r][c]
                    if inner_color!=out_color and not graph[out_color][inner_color]:
                        graph[out_color][inner_color]=True
                        indeg[inner_color]+=1
        q=deque([i for i in colors if indeg[i]==0])
        while q:
            out_color=q.popleft()
            colors.remove(out_color)
            for inner_color in colors:
                if graph[out_color][inner_color]:
                    indeg[inner_color]-=1
                    if indeg[inner_color]==0:
                        q.append(inner_color)
        return len(colors)==0
# @lc code=end
assert Solution().isPrintable(targetGrid = [[1,1,1],[3,1,3]])==False
assert Solution().isPrintable(targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]])

assert Solution().isPrintable([[1,1,1,1,3,1,1,1],[1,1,1,1,3,1,1,1],[1,1,1,1,3,1,1,1],[1,1,1,1,3,2,2,2],[1,1,1,1,3,2,2,2],[1,1,1,1,3,1,1,1],[1,1,1,1,1,1,4,4],[1,6,6,6,6,6,6,1],[1,6,6,6,6,6,6,1]])
assert Solution().isPrintable(targetGrid = [[1,2,1],[2,1,2],[1,2,1]])==False
assert Solution().isPrintable(targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]])