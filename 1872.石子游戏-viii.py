#
# @lc app=leetcode.cn id=1872 lang=python3
#
# [1872] 石子游戏 VIII
#
from sbw import *


# @lc code=start
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        presums = list(accumulate(stones, initial=0))
        N = len(stones)

        f=[0]*N
        f[-1]=presums[-1]
        for i in range(N-2,0,-1):
            f[i]=max(f[i+1],presums[i+1]-f[i+1])

        return f[1]
# @lc code=end
assert Solution().stoneGameVIII([7, -6, 5, 10, 5, -2, -6]) == 13
assert Solution().stoneGameVIII([-1, 2, -3, 4, -5]) == 5
