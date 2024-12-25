#
# @lc app=leetcode.cn id=2335 lang=python3
# @lcpr version=30204
#
# [2335] 装满杯子需要的最短总时长
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        a, b, c = amount
        if c >= a + b:
            return c
        return (a+b+c+1)//2


# @lc code=end
assert Solution().fillCups([3,5,3]) == 6
assert Solution().fillCups([5, 0, 0]) == 5
assert Solution().fillCups([5, 4, 4]) == 7
assert Solution().fillCups([1, 4, 2]) == 4


#
# @lcpr case=start
# [1,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,4]\n
# @lcpr case=end

# @lcpr case=start
# [5,0,0]\n
# @lcpr case=end

#
