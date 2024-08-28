#
# @lc app=leetcode.cn id=1920 lang=python3
# @lcpr version=30204
#
# [1920] 基于排列构建数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]+=1000*(nums[nums[i]]%1000)
        for i in range(len(nums)):
            nums[i]//=1000
        return nums
            

# @lc code=end
assert Solution().buildArray([0,2,1,5,3,4])==[0,1,2,4,5,3]


#
# @lcpr case=start
# [0,2,1,5,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [5,0,1,2,3,4]\n
# @lcpr case=end

#

