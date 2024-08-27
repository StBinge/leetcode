#
# @lc app=leetcode.cn id=3130 lang=python3
# @lcpr version=30204
#
# [3130] 找出所有稳定的二进制数组 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        f0 = [[0] * (one + 1) for _ in range(zero + 1)]
        f1 = [[0] * (one + 1) for _ in range(zero + 1)]
        for i in range(1, min(limit,zero)+1):
            f0[i][0] = 1
        for i in range(1, min(limit,one) + 1):
            f1[0][i] = 1

        mod = 10**9 + 7
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                f0[i][j] = f0[i - 1][j] + f1[i - 1][j]
                if i > limit:
                    f0[i][j] -= f1[i - limit - 1][j]
                f0[i][j] %= mod

                f1[i][j] = f1[i][j - 1] + f0[i][j - 1]
                if j > limit:
                    f1[i][j] -= f0[i][j - limit - 1]
                f1[i][j] %= mod
        return (f1[-1][-1] + f0[-1][-1]) % mod


# @lc code=end
assert Solution().numberOfStableArrays(1, 2, 1) == 1


#
# @lcpr case=start
# 1\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n2\n
# @lcpr case=end

#
