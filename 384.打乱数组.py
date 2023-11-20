#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#
from typing import List
# @lc code=start
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.origin=nums
        self.nums=nums.copy()

    def reset(self) -> List[int]:
        self.nums=self.origin.copy()
        return self.origin

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j=random.randint(i,len(self.nums)-1)
            self.nums[i],self.nums[j]=self.nums[j],self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

