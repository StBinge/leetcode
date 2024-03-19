#
# @lc app=leetcode.cn id=1276 lang=python3
#
# [1276] 不浪费原料的汉堡制作方案
#
from sbw import *
# @lc code=start
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices<2*cheeseSlices or tomatoSlices> cheeseSlices*4 or tomatoSlices%2:
            return []
        
        x=(tomatoSlices-2*cheeseSlices)//2
        y=cheeseSlices-x
        return [x,y]
# @lc code=end
assert Solution().numOfBurgers(2537427,860448)==[]
assert Solution().numOfBurgers(2,1)==[0,1]
assert Solution().numOfBurgers(0,0)==[0,0]
assert Solution().numOfBurgers(4,17)==[]
assert Solution().numOfBurgers(17,4)==[]
assert Solution().numOfBurgers(16,7)==[1,6]
