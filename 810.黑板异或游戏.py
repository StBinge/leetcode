#
# @lc app=leetcode.cn id=810 lang=python3
#
# [810] 黑板异或游戏
#
from typing import List
# @lc code=start
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums)%2==0:
            return True
        xor=0
        for n in nums:
            xor^=n
        return xor==0
# @lc code=end

