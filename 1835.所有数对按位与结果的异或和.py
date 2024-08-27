#
# @lc app=leetcode.cn id=1835 lang=python3
#
# [1835] 所有数对按位与结果的异或和
#
from sbw import *
# @lc code=start
import operator
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(operator.xor,arr1,0) & reduce(operator.xor,arr2,0)
# @lc code=end
assert Solution().getXORSum(arr1 = [1,2,3], arr2 = [6,5])==0
