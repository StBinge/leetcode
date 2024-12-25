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
        mx_dif=nums[0]-nums[1]
        pre_mx=max(nums[:2])
        ret=0
        for n in nums[2:]:
            ret=max(n*mx_dif,ret)
            mx_dif=max(mx_dif,pre_mx-n)
            pre_mx=max(pre_mx,n)
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

