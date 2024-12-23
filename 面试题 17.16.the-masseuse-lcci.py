#
# @lc app=leetcode.cn id=面试题 17.16 lang=python3
# @lcpr version=30204
#
# [面试题 17.16] 按摩师
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        f0,f1=0,nums[0]
        for i in range(1,len(nums)):
            f0,f1=max(f1,f0),f0+nums[i]
        return max(f0,f1)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,4,5,3,1,1,3]\n
# @lcpr case=end

#

