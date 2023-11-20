#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#

# @lc code=start
import math
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        a,b=max(jug1Capacity,jug2Capacity),min(jug1Capacity,jug2Capacity)
        c=a+b
        while c:
            if c==targetCapacity:
                return True
            if c>=b:
                c-=b
            else:
                c+=a
        return False
        

        
# @lc code=end

assert Solution().canMeasureWater(3,5,4)
assert Solution().canMeasureWater(2,6,5)==False
assert Solution().canMeasureWater(1,2,3)