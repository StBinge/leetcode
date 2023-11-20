#
# @lc app=leetcode.cn id=478 lang=python3
#
# [478] 在圆内随机生成点
#
from typing import List
# @lc code=start
import random,math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.center=(x_center,y_center)
        self.r=radius

    def randPoint(self) -> List[float]:
        rr=math.sqrt(random.random())*self.r
        angle=random.random()*2*math.pi
        x=math.cos(angle)*rr
        y=math.sin(angle)*rr
        return [x+self.center[0],y+self.center[1]]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end

