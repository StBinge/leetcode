#
# @lc app=leetcode.cn id=3074 lang=python3
#
# [3074] 重新分装苹果
#
from sbw import *
# @lc code=start
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s=sum(apple)
        capacity.sort(reverse=True)
        for i, cap in enumerate(capacity):
            s-=cap
            if s<=0:
                return i+1
# @lc code=end

assert Solution().minimumBoxes(apple = [1,3,2], capacity = [4,3,1,5,2])==2