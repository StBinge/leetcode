#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#
from sbw import *
# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter=Counter(nums)
        return sorted(nums,key=lambda x:(counter[x],-x))
# @lc code=end

