#
# @lc app=leetcode.cn id=1411 lang=python3
#
# [1411] 给 N x 3 网格图涂色的方案数
#

# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        f2=f3=6
        Mod=10**9+7
        for _ in range(n-1):
            f2,f3=f3*2+f2*3,f3*2+f2*2
            f2%=Mod
            f3%=Mod
        return (f2+f3)%Mod
# @lc code=end
assert Solution().numOfWays(5000)==30228214
assert Solution().numOfWays(7)==106494
assert Solution().numOfWays(3)==246
assert Solution().numOfWays(2)==54
assert Solution().numOfWays(1)==12
