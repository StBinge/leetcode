#
# @lc app=leetcode.cn id=2908 lang=python3
# @lcpr version=30204
#
# [2908] 元素和最小的山形三元组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N=len(nums)
        right_mi=[nums[-1]]*N
        for i in range(N-2,-1,-1):
            right_mi[i]=min(right_mi[i+1],nums[i])
        left_mi=nums[0]
        ret=200
        for i in range(1,N-1):
            if nums[i]>left_mi and nums[i]>right_mi[i+1]:
                ret=min(ret,nums[i]+left_mi+right_mi[i+1])
            left_mi=min(left_mi,nums[i])
        return ret if ret<200 else -1
# @lc code=end



#
# @lcpr case=start
# [8,6,1,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,7,10,2]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,4,3,4,5]\n
# @lcpr case=end

#

