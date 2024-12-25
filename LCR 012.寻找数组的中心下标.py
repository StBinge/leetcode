#
# @lc app=leetcode.cn id=LCR 012 lang=python3
# @lcpr version=30204
#
# [LCR 012] 寻找数组的中心下标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        left=0
        for i,n in enumerate(nums):
            if s-n-left==left:
                return i
            left+=n
        return -1
# @lc code=end



#
# @lcpr case=start
# [1,7,3,6,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3]\n
# @lcpr case=end

# @lcpr case=start
# [2, 1, -1]\n
# @lcpr case=end

#

