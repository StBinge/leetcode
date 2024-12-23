#
# @lc app=leetcode.cn id=2909 lang=python3
# @lcpr version=30204
#
# [2909] 元素和最小的山形三元组 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N=len(nums)
        left_mi=[0]*N
        right_mi=[0]*N
        lmi=nums[0]
        rmi=nums[-1]
        for i in range(N):
            lmi=min(lmi,nums[i])
            left_mi[i]=lmi
            rmi=min(rmi,nums[-1-i])
            right_mi[-1-i]=rmi
        ret=float('inf')
        for i in range(1,N):
            if nums[i]>left_mi[i] and nums[i]>right_mi[i]:
                ret=min(ret,nums[i]+left_mi[i]+right_mi[i])
        return ret if ret<float('inf') else -1
# @lc code=end
assert Solution().minimumSum([8,6,1,5,3])==9


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

