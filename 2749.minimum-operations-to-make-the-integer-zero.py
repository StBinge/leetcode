#
# @lc app=leetcode.cn id=2749 lang=python3
# @lcpr version=30204
#
# [2749] 得到整数零需要执行的最少操作数
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        cnt = 1
        while True:
            dif = num1 - cnt * num2
            if dif <= 0 or cnt>dif:
                return -1
            if dif.bit_count() <= cnt:
                return cnt
            cnt += 1

# @lc code=end
assert Solution().makeTheIntegerZero(85,42) == -1
assert Solution().makeTheIntegerZero(110,55) == -1
assert Solution().makeTheIntegerZero(5, 7) == -1
assert Solution().makeTheIntegerZero(3, -2) == 3


#
# @lcpr case=start
# 3\n-2\n
# @lcpr case=end

# @lcpr case=start
# 5\n7\n
# @lcpr case=end

#
