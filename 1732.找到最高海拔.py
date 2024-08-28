#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#
from sbw import *
# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur=0
        ret=0
        for g in gain:
            cur+=g
            ret=max(ret,cur)
        return ret
# @lc code=end
assert Solution().largestAltitude([-5,1,5,0,-7])==1
