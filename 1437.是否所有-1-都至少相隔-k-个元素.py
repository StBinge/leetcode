#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#
from sbw import *
# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre=-k-1
        for i,n in enumerate(nums):
            if n==1:
                if i-pre-1<k:
                    return False
                pre=i
        return True
# @lc code=end
assert Solution().kLengthApart(nums = [1,0,0,1,0,1], k = 2)==False
assert Solution().kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2)
