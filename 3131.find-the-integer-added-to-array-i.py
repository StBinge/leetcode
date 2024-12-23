#
# @lc app=leetcode.cn id=3131 lang=python3
# @lcpr version=30204
#
# [3131] 找出与数组相加的整数 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2)-min(nums1)

# @lc code=end



#
# @lcpr case=start
# [2,6,4]\n[9,7,5]\n
# @lcpr case=end

# @lcpr case=start
# [10]\n[5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n[1,1,1,1]\n
# @lcpr case=end

#

