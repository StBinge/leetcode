#
# @lc app=leetcode.cn id=1510 lang=python3
#
# [1510] 石子游戏 IV
#
from sbw import *
# @lc code=start
import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        f=[False]*(n+1)
        for i in range(1,n+1):
            j=1
            while (cubic:=j*j)<=i:
                if f[i-cubic]==False:
                    f[i]=True
                    break
                j+=1
        return f[-1]

# @lc code=end
assert Solution().winnerSquareGame(8)
assert Solution().winnerSquareGame(17)==False
assert Solution().winnerSquareGame(7)==False
assert Solution().winnerSquareGame(4)
assert Solution().winnerSquareGame(2)==False
assert Solution().winnerSquareGame(1)
