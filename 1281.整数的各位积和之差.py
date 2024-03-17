#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod,s=1,0
        while n>0:
            d=n%10
            prod*=d
            s+=d
            n//=10
        return prod-s
# @lc code=end
assert Solution().subtractProductAndSum(4421)==21
assert Solution().subtractProductAndSum(234)==15
