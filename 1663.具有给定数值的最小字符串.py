#
# @lc app=leetcode.cn id=1663 lang=python3
#
# [1663] 具有给定数值的最小字符串
#
import itertools

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        z_cnt,remain=divmod(k-n,25)
        if z_cnt==n:
            return 'z'*z_cnt
        return 'a'*(n-z_cnt-1) + chr(ord('a')+remain)+'z'*z_cnt
            
# @lc code=end
assert Solution().getSmallestString(5,130)=='zzzzz'
assert Solution().getSmallestString(5,73)=='aaszz'
assert Solution().getSmallestString(3,27)=='aay'
