#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#
from sbw import *
# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ret=set()
        v1=1
        for _ in range(20):
            if v1>=bound:
                break
            v2=1

            bound2=bound-v1
            for _ in range(20):
                if v2>bound2:
                    break
                ret.add(v1+v2)
                v2*=y
            v1*=x
        return list(ret)
# @lc code=end
x = 1
y = 1
bound = 10
ret=[2]
assert sorted(Solution().powerfulIntegers(x,y,bound))==sorted(ret)

x = 2
y = 1
bound = 10
ret=[9,2,3,5]
assert sorted(Solution().powerfulIntegers(x,y,bound))==sorted(ret)

x = 3
y = 5
bound = 15
ret=[2,4,6,8,10,14]
assert sorted(Solution().powerfulIntegers(x,y,bound))==ret

x = 2
y = 3
bound = 10
ret=[2,3,4,5,7,9,10]
assert sorted(Solution().powerfulIntegers(x,y,bound))==ret