#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#
from sbw import *
# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target)==Counter(arr)
        
# @lc code=end
assert Solution().canBeEqual([1,4,2,3],[1,4,2,3])
assert Solution().canBeEqual([1,2,2,3],[1,1,2,3])==False
