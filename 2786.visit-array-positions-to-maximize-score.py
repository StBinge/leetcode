#
# @lc app=leetcode.cn id=2786 lang=python3
# @lcpr version=30204
#
# [2786] 访问数组中的位置使分数最大
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        f=[0,0]
        for n in reversed(nums):
            r=n&1
            f[r]=max(f[r],f[r^1]-x)+n
        return f[nums[0]&1]
            

# @lc code=end
assert Solution().maxScore([8,50,65,85,8,73,55,50,29,95,5,68,52,79],74)==470
assert Solution().maxScore(nums = [2,4,6,8], x = 3)==20
assert Solution().maxScore(nums = [2,3,6,1,9,2], x = 5)==13


#
# @lcpr case=start
# [2,3,6,1,9,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6,8]\n3\n
# @lcpr case=end

#

