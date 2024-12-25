#
# @lc app=leetcode.cn id=3192 lang=python3
# @lcpr version=30204
#
# [3192] 使二进制数组全部等于 1 的最少操作次数 II
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # N=len(nums)
        ret=0
        for bit in nums:
            if bit==ret%2:
                ret+=1
        return ret
        
# @lc code=end
assert Solution().minOperations([0,1,1,0,1])==4


#
# @lcpr case=start
# [0,1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,0]\n
# @lcpr case=end

#

