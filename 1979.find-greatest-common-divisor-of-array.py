#
# @lc app=leetcode.cn id=1979 lang=python3
# @lcpr version=30204
#
# [1979] 找出数组的最大公约数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(max(nums),min(nums))
# @lc code=end



#
# @lcpr case=start
# [2,5,6,9,10]\n
# @lcpr case=end

# @lcpr case=start
# [7,5,6,8,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n
# @lcpr case=end

#

