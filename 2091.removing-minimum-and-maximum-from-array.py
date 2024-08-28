#
# @lc app=leetcode.cn id=2091 lang=python3
# @lcpr version=30204
#
# [2091] 从数组中移除最大值和最小值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi=float('inf')
        mx=float('-inf')
        idx1=idx2=-1
        for i,n in enumerate(nums):
            if n<mi:
                mi=n
                idx1=i
            if n>mx:
                mx=n
                idx2=i
        N=len(nums)
        if idx1>idx2:
            idx1,idx2=idx2,idx1
        return min(idx2+1,N-idx1,idx1+1+N-idx2)
# @lc code=end



#
# @lcpr case=start
# [2,10,7,5,4,1,8,6]\n
# @lcpr case=end

# @lcpr case=start
# [0,-4,19,1,8,-2,-3,5]\n
# @lcpr case=end

# @lcpr case=start
# [101]\n
# @lcpr case=end

#

