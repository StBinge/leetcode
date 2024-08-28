#
# @lc app=leetcode.cn id=1760 lang=python3
#
# [1760] 袋子里最少数目的球
#
from sbw import *
# @lc code=start
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left=1
        right=10**9
        while left<right:
            mid=(left+right)>>1
            op=sum((n-1)//mid for n in nums)
            if op>maxOperations:
                left=mid+1
            else:
                right=mid
        return left

# @lc code=end
assert Solution().minimumSize(nums = [7,17], maxOperations = 2)==7
assert Solution().minimumSize(nums = [2,4,8,2], maxOperations = 4)==2
assert Solution().minimumSize([9],2)==3
