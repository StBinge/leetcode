#
# @lc app=leetcode.cn id=2592 lang=python3
# @lcpr version=30204
#
# [2592] 最大化数组的伟大值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        return len(nums)-max(Counter(nums).values())
# @lc code=end



#
# @lcpr case=start
# [1,3,5,2,1,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#

