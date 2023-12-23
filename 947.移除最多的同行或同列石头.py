#
# @lc app=leetcode.cn id=947 lang=python3
#
# [947] 移除最多的同行或同列石头
#
from sbw import *
# @lc code=start
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_ys={}
        y_xs={}
        for stone in stones:
            s=tuple(stone)
            x_ys.setdefault(stone[0],[]).append(s)
            y_xs.setdefault(stone[1],[]).append(s)
        
        vis=set()
        def dfs(stone):
            if stone in vis:
                return
            vis.add(stone)
            for s in x_ys[stone[0]]:
                dfs(s)
            for s in y_xs[stone[1]]:
                dfs(s)
        
        ret=0
        for s in stones:
            t=tuple(s)
            if t not in vis:
                ret+=1
                dfs(t)
        return len(stones)-ret
        

# @lc code=end
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
assert Solution().removeStones(stones)==3

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
assert Solution().removeStones(stones)==5
stones = [[0,0]]
assert Solution().removeStones(stones)==0
