#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#
from typing import List
# @lc code=start
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for w in range(int(math.sqrt(area)),0,-1):
            if area % w==0:
                return [area//w,w]
        
# @lc code=end

assert Solution().constructRectangle(2)==[2,1]
assert Solution().constructRectangle(4)==[2,2]
assert Solution().constructRectangle(37)==[37,1]
assert Solution().constructRectangle(122122)==[427,286]