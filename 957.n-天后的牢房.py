#
# @lc app=leetcode.cn id=957 lang=python3
#
# [957] N 天后的牢房
#
from sbw import *
# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        vis={}

        while n>0:
            t=tuple(cells)
            pre=vis.get(t,-1)
            if pre>0:
                n%=pre-n
            vis[t]=n
            if n>0:
                n-=1
                cells=[int(0<i<7 and cells[i-1] == cells[i+1]) for i in range(8)]
        return cells
# @lc code=end
cells = [1,0,0,1,0,0,1,0]
n = 1000000000
ret=[0,0,1,1,1,1,1,0]
assert Solution().prisonAfterNDays(cells,n)==ret

cells = [0,1,0,1,1,0,0,1]
n = 7
ret=[0,0,1,1,0,0,0,0]
assert Solution().prisonAfterNDays(cells,n)==ret
