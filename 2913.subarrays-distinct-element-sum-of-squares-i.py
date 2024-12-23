#
# @lc app=leetcode.cn id=2913 lang=python3
# @lcpr version=30204
#
# [2913] 子数组不同元素数目的平方和 I
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        N=len(nums)
        ret=0
        for i in range(N):
            s=set()
            for j in range(i,N):
                s.add(nums[j])
                ret+=len(s)**2
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2]\n
# @lcpr case=end

#

