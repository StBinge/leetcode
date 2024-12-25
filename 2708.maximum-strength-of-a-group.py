#
# @lc app=leetcode.cn id=2708 lang=python3
# @lcpr version=30204
#
# [2708] 一个小组的最大实力值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        mi=mx=nums[0]
        # zero=False
        for n in nums[1:]:
            _mi=min(mi,mi*n,mx*n,n)
            _mx=max(mx,mx*n,mi*n,n)
            mi=_mi
            mx=_mx

        return mx
# @lc code=end
assert Solution().maxStrength([-4,-5,-4])==20
assert Solution().maxStrength([3,-1,-5,2,5,-9])==1350
assert Solution().maxStrength([0,-1])==0


#
# @lcpr case=start
# [3,-1,-5,2,5,-9]\n
# @lcpr case=end

# @lcpr case=start
# [-4,-5,-4]\n
# @lcpr case=end

#

