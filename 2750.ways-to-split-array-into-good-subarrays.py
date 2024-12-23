#
# @lc app=leetcode.cn id=2750 lang=python3
# @lcpr version=30204
#
# [2750] 将数组划分成若干好子数组的方式
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans, pre = 1, -1
        for i, x in enumerate(nums):
            if x == 0: continue
            if pre >= 0:
                ans = ans * (i - pre) % MOD
            pre = i
        return 0 if pre < 0 else ans

            

# @lc code=end
assert Solution().numberOfGoodSubarraySplits([1,0,0,0,0,0,1,0,1])==12
assert Solution().numberOfGoodSubarraySplits([0,1,0])==1
assert Solution().numberOfGoodSubarraySplits([0,1,0,0,1])==3


#
# @lcpr case=start
# [0,1,0,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

#

