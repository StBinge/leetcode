#
# @lc app=leetcode.cn id=2873 lang=python3
# @lcpr version=30204
#
# [2873] 有序三元组中的最大值 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        pre_max=max(nums[:2])
        max_dif=nums[0]-nums[1]
        ret=0
        for i in range(2,len(nums)):
            ret=max(ret,max_dif*nums[i])
            max_dif=max(max_dif,pre_max-nums[i])
            pre_max=max(pre_max,nums[i])
        return ret

# @lc code=end
assert Solution().maximumTripletValue([1,10,3,4,19])==133
assert Solution().maximumTripletValue([12,6,1,2,7])==77


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

