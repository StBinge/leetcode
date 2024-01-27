#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] 丑数 III
#

# @lc code=start
import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        g_ab=math.gcd(a,b)
        lcm_ab=a*b//g_ab
        g_bc=math.gcd(b,c)
        lcm_bc=b*c//g_bc
        g_ac=math.gcd(a,c)
        lcm_ac=a*c//g_ac
        lcm_abc=lcm_ab*c//(math.gcd(lcm_ab,c))

        left=min(a,b,c)
        right=left*n
        while left<right:
            mid=(left+right)>>1
            cnt=mid//a+mid//b+mid//c-mid//lcm_ab-mid//lcm_bc-mid//lcm_ac+mid//lcm_abc
            if cnt<n:
                left=mid+1
            else:
                right=mid
        return left-min(left%a,left%b,left%c)
# @lc code=end
assert Solution().nthUglyNumber(n = 4, a = 2, b = 3, c = 4)==6
assert Solution().nthUglyNumber(3,2,3,5)==4
