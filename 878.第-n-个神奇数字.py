#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#

# @lc code=start
import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:

        Mod=10**9+7
        c=math.lcm(a,b)
        m=c//a+c//b-1
        r=n%m
        res=(c*(n//m))%Mod
        if r==0:
            return res
        add_a=a
        add_b=b
        r-=1
        while r>0:
            if add_a<=add_b:
                add_a+=a
            else:
                add_b+=b
            r-=1
        return (res+min(add_a,add_b))%Mod
# @lc code=end
assert Solution().nthMagicalNumber(4,2,3)==6
assert Solution().nthMagicalNumber(1,2,3)==2
