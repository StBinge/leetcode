#
# @lc app=leetcode.cn id=2466 lang=python3
# @lcpr version=30204
#
# [2466] 统计构造好字符串的方案数
#


# @lcpr-template-start

from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        g=math.gcd(one,zero)
        low=(low-1)//g + 1
        high//=g
        zero//=g
        one//=g
        f = [0] * (high + 1)
        f[0] = 1
        Mod = 10**9 + 7
        for i in range(1, high + 1):
            if i >= zero:
                f[i] = f[i - zero]
            if i >= one:
                f[i] += f[i - one]
            f[i] %= Mod
        return sum(f[low:]) % Mod


# @lc code=end
assert Solution().countGoodStrings(low=2, high=3, zero=1, one=2) == 5
assert Solution().countGoodStrings(low=3, high=3, zero=1, one=1) == 8


#
# @lcpr case=start
# 3\n3\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# 2\n3\n1\n2\n
# @lcpr case=end

#
