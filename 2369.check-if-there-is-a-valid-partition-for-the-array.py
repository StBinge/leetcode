#
# @lc app=leetcode.cn id=2369 lang=python3
# @lcpr version=30204
#
# [2369] 检查数组是否存在有效划分
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # type1 =>0b001 1
        # type2 =>0b010 2
        # type3 =>0b100 4
        N=len(nums)
        f=[False]*(N+1)
        f[0]=True
        if nums[0]==nums[1]:
            f[2]=True
        for i in range(2,len(nums)):
            if (nums[i]==nums[i-1] and f[i-1]) or \
                (nums[i]==nums[i-1]==nums[i-2] and f[i-2]) or \
                (nums[i]==nums[i-1]+1 and nums[i]==nums[i-2]+2 and f[i-2]):
                f[i+1]=True
        return f[-1]

            

# @lc code=end
assert not Solution().validPartition([10,20,30])
assert not Solution().validPartition([1,1,1,2])
assert Solution().validPartition([4,4,4,5,6])


#
# @lcpr case=start
# [4,4,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2]\n
# @lcpr case=end

#

