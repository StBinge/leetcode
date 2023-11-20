#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#
from typing import List
# @lc code=start
import random
class Solution:

    def __init__(self, nums: List[int]):
        slots={}
        for i,n in enumerate(nums):
            pos=slots.setdefault(n,[])
            pos.append(i)
        self.slots=slots


    def pick(self, target: int) -> int:
        pos=self.slots[target]
        return random.choice(pos)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

