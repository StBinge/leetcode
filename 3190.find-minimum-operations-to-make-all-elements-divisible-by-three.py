#
# @lc app=leetcode.cn id=3190 lang=python3
# @lcpr version=30204
#
# [3190] 使所有元素都可以被 3 整除的最少操作数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(n%3!=0 for n in nums)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,6,9]\n
# @lcpr case=end

#

