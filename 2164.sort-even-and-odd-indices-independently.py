#
# @lc app=leetcode.cn id=2164 lang=python3
# @lcpr version=30204
#
# [2164] 对奇偶下标分别排序
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        N=len(nums)
        odds=nums[1:N:2]
        evens=nums[:N:2]
        nums[1:N:2]=sorted(odds,reverse=True)
        nums[::2]=sorted(evens)
        return nums
# @lc code=end



#
# @lcpr case=start
# [4,1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n
# @lcpr case=end

#

