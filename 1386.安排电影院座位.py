#
# @lc app=leetcode.cn id=1386 lang=python3
#
# [1386] 安排电影院座位
#
from sbw import *
# @lc code=start
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        used={}
        for row,col in reservedSeats:
            if col==1 or col==10:
                continue
            mask=used.get(row,0)
            mask |= 1<<(col-2)
            used[row]=mask
        
        ret=(n-len(used))*2
        left=0b1111_0000
        middle=0b1100_0011
        right=0b0000_1111
        for mask in used.values():
            if (mask | left)==left or (mask | middle)==middle or (mask | right)==right:
                ret+=1
        return ret
# @lc code=end
assert Solution().maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]])==2
assert Solution().maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]])==4
assert Solution().maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])==4
