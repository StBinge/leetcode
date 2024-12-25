#
# @lc app=leetcode.cn id=2342 lang=python3
# @lcpr version=30204
#
# [2342] 数位和相等数对的最大和
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mx=[0]*82
        ret=-1
        for i, n in enumerate(nums):
            s = 0
            while n:
                n, m = divmod(n, 10)
                s += m
            if mx[s]:
                ret=max(ret,nums[i]+mx[s])
            mx[s]=max(mx[s],nums[i])
        return ret


# @lc code=end
assert Solution().maximumSum([18,43,36,13,7])==54

#
# @lcpr case=start
# [18,43,36,13,7]\n
# @lcpr case=end

# @lcpr case=start
# [10,12,19,14]\n
# @lcpr case=end

#
