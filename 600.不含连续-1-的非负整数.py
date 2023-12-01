#
# @lc app=leetcode.cn id=600 lang=python3
#
# [600] 不含连续1的非负整数
#

# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0]*31
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 31):
            dp[i] = dp[i-1]+dp[i-2]

        ret = 0
        pre = 0
        for i in range(29, -1, -1):
            bits = 1 << i
            if n & bits:
                ret += dp[i]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0
            if i == 0:
                ret += 1
        return ret

# @lc code=end



assert Solution().findIntegers(6) == 5
assert Solution().findIntegers(5) == 5
assert Solution().findIntegers(1000000000) == 2178309
assert Solution().findIntegers(1) == 2
assert Solution().findIntegers(2) == 3
