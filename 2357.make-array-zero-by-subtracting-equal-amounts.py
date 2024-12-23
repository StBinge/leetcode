#
# @lc app=leetcode.cn id=2357 lang=python3
# @lcpr version=30204
#
# [2357] 使数组中所有元素都等于零
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen=set()
        for n in nums:
            if n>0:
                seen.add(n)
        return len(seen)
# @lc code=end



#
# @lcpr case=start
# [1,5,0,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

