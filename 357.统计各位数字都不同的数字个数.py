#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 统计各位数字都不同的数字个数
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        
        
        pre=1
        cur=9
        for i in range(n-1):
            pre+=cur
            cur*=(9-i)
        return pre+cur
# @lc code=end
assert Solution().countNumbersWithUniqueDigits(2)==91
assert Solution().countNumbersWithUniqueDigits(1)==10
assert Solution().countNumbersWithUniqueDigits(0)==1
