#
# @lc app=leetcode.cn id=1690 lang=python3
#
# [1690] 石子游戏 VII
#
from sbw import *


# @lc code=start
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)
        W = [0]
        for s in stones:
            W.append(s + W[-1])

        f=[0]*N
        for i in range(N-1,-1,-1):
            for j in range(i+1,N):
                f[j]=max(W[j+1]-W[i+1]-f[j],W[j]-W[i]-f[j-1])
        return f[-1]
# @lc code=end
assert Solution().stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]) == 122
assert Solution().stoneGameVII([5, 3, 1, 4, 2]) == 6
