#
# @lc app=leetcode.cn id=3194 lang=python3
# @lcpr version=30204
#
# [3194] 最小元素和最大元素的最小平均值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        return min(nums[i]+nums[-1-i] for i in range(len(nums)//2))/2
# @lc code=end



#
# @lcpr case=start
# [7,8,3,4,15,13,4,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,9,8,3,10,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,7,8,9]\n
# @lcpr case=end

#

