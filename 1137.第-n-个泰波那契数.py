#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<3:
            return [0,1,1][n]
        x,y,z=0,1,1
        for i in range(3,n+1):
            x,y,z=y,z,x+y+z
        return z
# @lc code=end
assert Solution().tribonacci(25)==1389537
assert Solution().tribonacci(4)==4
