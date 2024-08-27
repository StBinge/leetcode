#
# @lc app=leetcode.cn id=1745 lang=python3
#
# [1745] 分割回文串 IV
#


# @lc code=start
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        ss = s
        s = "$" + "$".join(s) + "$"
        N = len(s)
        f = [1] * N
        L, R = 0, 0
        idx = 0
        while idx < N:
            l = 1
            if idx <= R:
                _idx = 2 * L - idx
                if f[_idx] < R - idx + 1:
                    f[idx] = f[_idx]
                    idx += 1
                    continue

                l = R - idx + 1
            while idx + l < N and idx - L >= 0 and s[idx + l] == s[idx - l]:
                l += 1
            f[idx] = l

            R = idx + l - 1
            L = idx
            idx += 1
        # N=len(ss)
        for i in range(1, N - 1):
            l1 = i
            if l1<3:
                continue
            c1 = l1 // 2
            if f[c1] * 2 - 1 != l1:
                continue
            for j in range(i + 1, N):
                l3 = N - j
                if l3<3:
                    continue
                c3 = l3 // 2 + j
                if f[c3] * 2 - 1 != l3:
                    continue
                l2 = j - i
                c2 = l2 // 2 + i
                if f[c2] * 2 - 1 >= l2:
                    return True
        return False


# @lc code=end
assert Solution().checkPartitioning("acab") == False
assert Solution().checkPartitioning("bcbddxy") == False
assert Solution().checkPartitioning("abcbdd")
