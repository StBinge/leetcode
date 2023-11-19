#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#
from typing import List
# @lc code=start
import random
class Solution:

    def __init__(self, w: List[int]):
        self.presum=[0]
        for n in w:
            self.presum.append(n+self.presum[-1])

    def pickIndex(self) -> int:
        # if len(self.presum)
        x=random.randrange(self.presum[-1])
        left,right=0,len(self.presum)
        while left<right:
            mid=(left+right)//2
            if self.presum[mid]>x:
                right=mid
            else:
                left=mid+1
        return left-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

