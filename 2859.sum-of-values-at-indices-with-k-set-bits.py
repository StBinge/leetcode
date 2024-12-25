#
# @lc app=leetcode.cn id=2859 lang=python3
# @lcpr version=30204
#
# [2859] 计算 K 置位下标对应元素的和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(n for i,n in enumerate(nums) if i.bit_count()==k)
# @lc code=end



#
# @lcpr case=start
# [5,10,1,5,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n2\n
# @lcpr case=end

#

