#
# @lc app=leetcode.cn id=2997 lang=python3
# @lcpr version=30204
#
# [2997] 使数组异或和等于 K 的最少操作次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return reduce(lambda x,y:x^y,nums,k).bit_count()
# @lc code=end



#
# @lcpr case=start
# [2,1,3,4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,0,2,0]\n0\n
# @lcpr case=end

#

