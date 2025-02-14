#
# @lc app=leetcode.cn id=3392 lang=python3
# @lcpr version=30204
#
# [3392] 统计符合条件长度为 3 的子数组数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(nums[i]==(nums[i-1]+nums[i+1])*2 for i in range(1,len(nums)-1))
# @lc code=end



#
# @lcpr case=start
# [1,2,1,4,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

#

