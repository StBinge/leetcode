#
# @lc app=leetcode.cn id=1503 lang=python3
#
# [1503] 所有蚂蚁掉下来前的最后一刻
#
from sbw import *
# @lc code=start
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ret=0
        if left:
            ret=max(left)
        if right:
            ret=max(ret,n-min(right))
        return ret
# @lc code=end
assert Solution().getLastMoment(7,[],[0,1,2,3,4,5,6,7])==7
assert Solution().getLastMoment(n = 4, left = [4,3], right = [0,1])==4
