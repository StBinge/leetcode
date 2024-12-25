#
# @lc app=leetcode.cn id=3191 lang=python3
# @lcpr version=30204
#
# [3191] 使二进制数组全部等于 1 的最少操作次数 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                ret+=1
                nums[i+1]^=1
                nums[i+2]^=1
        return ret if (nums[-1]==nums[-2]==1) else -1

# @lc code=end



#
# @lcpr case=start
# [0,1,1,1,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1]\n
# @lcpr case=end

#

