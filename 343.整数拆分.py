#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n<4:
            return n-1
        q,r=n//3, n%3
        if r==0:
            return 3**q
        if r==1:
            return 3**(q-1)*4
        return 3**q*2
# @lc code=end
assert Solution().integerBreak(8)==18
assert Solution().integerBreak(10)==36
assert Solution().integerBreak(2)==1
