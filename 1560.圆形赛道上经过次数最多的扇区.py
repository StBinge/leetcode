#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#
from sbw import *


# @lc code=start
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        l=rounds[0]
        r=rounds[-1]
        if l<=r:
            return [i for i in range(l,r+1)]
        return [i for i in range(1,r+1)]+[i for i in range(l,n+1)]


# @lc code=end
assert Solution().mostVisited(3,[3,2,1,2,1,3,2,1,2,1,3,2,3,1]) == [1,3]
assert Solution().mostVisited(n = 7, rounds = [1,3,5,7]) == [1,2,3,4,5,6,7]
assert Solution().mostVisited(n = 2, rounds = [2,1,2,1,2,1,2,1,2]) == [2]
assert Solution().mostVisited(n=4, rounds=[1, 3, 1, 2]) == [1, 2]
