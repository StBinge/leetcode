#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#
from sbw import *
# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x:(x.bit_count(),x))
        return arr
# @lc code=end
assert Solution().sortByBits([0,1,2,3,4,5,6,7,8])==[0,1,2,4,8,3,5,6,7]
