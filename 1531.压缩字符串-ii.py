#
# @lc app=leetcode.cn id=1531 lang=python3
#
# [1531] 压缩字符串 II
#
from sbw import *


# @lc code=start
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def cost(cnt):
            if cnt == 1:
                return 1
            elif cnt < 10:
                return 2
            elif cnt < 100:
                return 3
            return 4

        N = len(s)
        f = [[100] * (k + 1) for _ in range(N + 1)]
        f[0]=[0]*(k+1)
        for i in range(1, N + 1):
            for j in range(min(i, k) + 1):
                if j > 0:
                    f[i][j] = f[i - 1][j - 1]
                same = 0
                not_same = 0
                for i0 in range(i - 1, -1, -1):
                    if s[i - 1] == s[i0]:
                        same += 1
                        f[i][j] = min(f[i][j], f[i0][j - not_same] + cost(same))
                    else:
                        not_same += 1
                        if not_same > j:
                            break
        return f[-1][-1]


# @lc code=end
assert Solution().getLengthOfOptimalCompression(s="aaabcccd", k=2) == 4
assert Solution().getLengthOfOptimalCompression(s="aabbaa", k=2) == 2
assert (
    Solution().getLengthOfOptimalCompression(s="abcdefghijklmnopqrstuvwxyz", k=16) == 10
)
assert Solution().getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0) == 3
assert Solution().getLengthOfOptimalCompression(s="abc", k=2) == 1

