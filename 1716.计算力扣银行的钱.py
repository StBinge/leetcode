#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        w,day=divmod(n,7)
        ret=28*w+ 7*w*(w-1)//2+(w*2+1+day)*day//2
        return ret
# @lc code=end

assert Solution().totalMoney(20)==96
assert Solution().totalMoney(10)==37
assert Solution().totalMoney(4)==10