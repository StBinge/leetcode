#
# @lc app=leetcode.cn id=面试题 08.03 lang=python3
# @lcpr version=30204
#
# [面试题 08.03] 魔术索引
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            if i==n:
                return i
        return -1
# @lc code=end



#
# @lcpr case=start
# [0, 2, 3, 4, 5]\n
# @lcpr case=end

# @lcpr case=start
# [1, 1, 1]\n
# @lcpr case=end

#

