#
# @lc app=leetcode.cn id=858 lang=python3
#
# [858] 镜面反射
#

# @lc code=start
import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g=math.gcd(p,q)
        # v=p*q//g
        w=(p//g)%2
        h=(q//g)%2
        # if w%2:
        #     if h%2:
        #         return 1
        #     else:
        #         return 0
        # else:
        #     if h%2:
        #         return 2
        #     else:
        #         return 0
        if w and h:
            return 1
        elif h:
            return 2
        else:
            return 0

# @lc code=end

assert Solution().mirrorReflection(2,1)==2
assert Solution().mirrorReflection(3,2)==0
assert Solution().mirrorReflection(3,1)==1