#
# @lc app=leetcode.cn id=724 lang=python3
# @lcpr version=30204
#
# [724] 寻找数组的中心下标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)
        for i,n in enumerate(nums):
            right-=n
            if left==right:
                return i
            left+=n
        return -1

# @lc code=end



#
# @lcpr case=start
# [1, 7, 3, 6, 5, 6]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3]\n
# @lcpr case=end

# @lcpr case=start
# [2, 1, -1]\n
# @lcpr case=end

#

