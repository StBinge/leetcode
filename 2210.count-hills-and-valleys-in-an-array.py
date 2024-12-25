#
# @lc app=leetcode.cn id=2210 lang=python3
# @lcpr version=30204
#
# [2210] 统计数组中峰和谷的数量
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        pre = nums[0]
        ret = 0
        flag = 0
        for n in nums[1:]:
            if n > pre:
                if flag == -1:
                    ret += 1
                flag = 1
            elif n < pre:
                if flag == 1:
                    ret += 1
                flag = -1
            pre = n
        return ret


# @lc code=end

assert Solution().countHillValley([6, 6, 5, 5, 4, 1]) == 0

#
# @lcpr case=start
# [2,4,1,1,6,5]\n
# @lcpr case=end

# @lcpr case=start
# [6,6,5,5,4,1]\n
# @lcpr case=end

#
