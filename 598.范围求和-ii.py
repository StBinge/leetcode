#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#
from typing import List
# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a,b=m,n
        for r,c in ops:
            a=min(a,r)
            b=min(b,c)
        return a*b
# @lc code=end
m = 3
n = 3
ops = [[2,2],[3,3]]
assert Solution().maxCount(m,n,ops)==4

ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
assert Solution().maxCount(m,n,ops)==4

ops = []
assert Solution().maxCount(m,n,ops)==9


