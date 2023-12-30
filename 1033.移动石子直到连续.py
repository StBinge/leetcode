#
# @lc app=leetcode.cn id=1033 lang=python3
#
# [1033] 移动石子直到连续
#
from sbw import *
# @lc code=start
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c=sorted([a,b,c])
        if a+1==b and b+1==c:
            return [0,0]
        max_move=c-a-2
        min_gap=min(b-a,c-b)-1
        if min_gap<2:
            min_move=1
        else:
            min_move=2
        return [min_move,max_move]
# @lc code=end
assert Solution().numMovesStones(1,9,5)==[2,6]
assert Solution().numMovesStones(3,5,1)==[1,2]
assert Solution().numMovesStones(1,2,5)==[1,2]
assert Solution().numMovesStones(4,3,2)==[0,0]
