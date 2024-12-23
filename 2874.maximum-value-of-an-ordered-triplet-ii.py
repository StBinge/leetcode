#
# @lc app=leetcode.cn id=2874 lang=python3
# @lcpr version=30204
#
# [2874] 有序三元组中的最大值 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N=len(nums)
        mx_dif=0
        ret=0
        mx=nums[0]
        for i in range(1,N-1):
            mx_dif=max(mx_dif,mx-nums[i])
            ret=max(ret,mx_dif*nums[i+1])
            mx=max(mx,nums[i])
        return ret
# @lc code=end



#
# @lcpr case=start
# [12,6,1,2,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,10,3,4,19]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

