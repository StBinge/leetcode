#
# @lc app=leetcode.cn id=2656 lang=python3
# @lcpr version=30204
#
# [2656] K 个元素的最大和
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        return (mx+mx+k-1)*k//2
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5]\n2\n
# @lcpr case=end

#

