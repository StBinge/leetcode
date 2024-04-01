#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s=start>>1
        e=n&start&1
        def sumXor(x):
            m=x%4
            if m==0:
                return x
            elif m==1:
                return 1
            elif m==2:
                return x+1
            return 0
        
        return ((sumXor(s-1) ^ sumXor(s+n-1)) <<1)|e
# @lc code=end
assert Solution().xorOperation(4,3)==8
assert Solution().xorOperation(n = 5, start = 0)==8
