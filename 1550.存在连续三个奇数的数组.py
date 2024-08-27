#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#
from sbw import *


# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any((arr[i]&1 and arr[i+1]&1 and arr[i+2]&1) for i in range(len(arr)-2))


# @lc code=end
assert Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12])
assert Solution().threeConsecutiveOdds([2, 6, 4, 1]) == False
