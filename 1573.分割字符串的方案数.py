#
# @lc app=leetcode.cn id=1573 lang=python3
#
# [1573] 分割字符串的方案数
#


# @lc code=start
class Solution:
    def numWays(self, s: str) -> int:
        ones = s.count("1")
        n = len(s)
        if ones == 0:
            return (n - 1) * (n - 2) // 2 % (10**9 + 7)
        if ones % 3:
            return 0
        avg = ones // 3
        idx = 0
        cnt = 0
        while cnt < avg:
            if s[idx] == "1":
                cnt += 1
            idx += 1
        z1 = 0
        while s[idx] == "0":
            z1 += 1
            idx += 1

        idx = len(s) - 1
        cnt = 0
        while cnt < avg:
            if s[idx] == "1":
                cnt += 1
            idx -= 1
        z2 = 0
        while s[idx] == "0":
            z2 += 1
            idx -= 1
        return (z1 + 1) * (z2 + 1) % (10**9 + 7)


# @lc code=end
assert Solution().numWays("100100010100110") == 12
assert Solution().numWays("0000") == 3
assert Solution().numWays("1001") == 0
assert Solution().numWays("10101") == 4
