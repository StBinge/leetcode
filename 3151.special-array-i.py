#
# @lc app=leetcode.cn id=3151 lang=python3
# @lcpr version=30204
#
# [3151] 特殊数组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # if len(nums)==1:
        #     return True
        return all((x^y)&1 for x,y in pairwise(nums))
# @lc code=end



#
# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,6]\n
# @lcpr case=end

#

