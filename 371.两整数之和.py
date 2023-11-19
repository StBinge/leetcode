#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask1=2<<32
        mask2=2<<31
        mask3=mask2-1
        a%=mask1
        b%=mask1
        while b!=0:
            carray=(a&b)<<1
            carray%=mask1
            a=a^b
            b=carray
        
        if a&mask2:
            return ~((a^mask2)^mask3)
        else:
            return a
            

# @lc code=end
assert Solution().getSum(-1,4)==3
assert Solution().getSum(3,4)==7
assert Solution().getSum(3,2)==5
assert Solution().getSum(1,2)==3
