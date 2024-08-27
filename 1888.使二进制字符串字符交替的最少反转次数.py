#
# @lc app=leetcode.cn id=1888 lang=python3
#
# [1888] 使二进制字符串字符交替的最少反转次数
#


# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        N = len(s)
        half = N // 2
        even0 = sum(s[i] == "0" for i in range(0, N, 2))
        odd0 = sum(s[i] == "0" for i in range(1, N, 2))
        if N & 1 == 0:
            cnt = half - even0 + odd0
            return min(cnt, N - cnt)
        ret = N
        half += 1
        for i in range(N):
            cnt = half - even0 + odd0
            ret = min(ret, cnt, N - cnt)
            if s[i] == "0":
                even0 -= 1
                even0, odd0 = odd0, even0
                even0 += 1
            else:
                even0, odd0 = odd0, even0
        return ret


# @lc code=end
assert Solution().minFlips("1110") == 1
assert Solution().minFlips("010") == 0
assert Solution().minFlips("111000") == 2
