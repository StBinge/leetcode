#
# @lc app=leetcode.cn id=3105 lang=python3
# @lcpr version=30204
#
# [3105] 最长的严格递增或递减子数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        left_asc=0
        left_dec=0
        ret=1
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                ret=max(ret,i-left_asc)
                left_asc=i
            if nums[i]>=nums[i-1]:
                ret=max(ret,i-left_dec)
                left_dec=i
        return max(ret,len(nums)-left_asc,len(nums)-left_dec)


# @lc code=end



#
# @lcpr case=start
# [1,4,3,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#

