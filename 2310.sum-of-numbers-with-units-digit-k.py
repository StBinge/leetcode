#
# @lc app=leetcode.cn id=2310 lang=python3
# @lcpr version=30204
#
# [2310] 个位数字为 K 的整数之和
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            return 1 if num % 10==0 else -1

        for i in range(1, min(num // k + 1, 11)):
            if (num - i * k) % 10 == 0:
                return i
        return -1


# @lc code=end
assert Solution().minimumNumbers(30, 3) == 10
assert Solution().minimumNumbers(20, 1) == 10
assert Solution().minimumNumbers(10, 1) == 10
assert Solution().minimumNumbers(10, 8) == -1
assert Solution().minimumNumbers(2, 8) == -1
assert Solution().minimumNumbers(0, 7) == 0
assert Solution().minimumNumbers(37, 2) == -1
assert Solution().minimumNumbers(58, 9) == 2


#
# @lcpr case=start
# 58\n9\n
# @lcpr case=end

# @lcpr case=start
# 37\n2\n
# @lcpr case=end

# @lcpr case=start
# 0\n7\n
# @lcpr case=end

#
