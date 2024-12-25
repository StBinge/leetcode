#
# @lc app=leetcode.cn id=2270 lang=python3
# @lcpr version=30204
#
# [2270] 分割数组的方案数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s=sum(nums)
        left=0
        ret=0
        for i in range(len(nums)-1):
            left+=nums[i]
            s-=nums[i]
            if left>=s:
                ret+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [10,4,-8,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,1,0]\n
# @lcpr case=end

#

