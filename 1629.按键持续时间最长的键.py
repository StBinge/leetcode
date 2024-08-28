#
# @lc app=leetcode.cn id=1629 lang=python3
#
# [1629] 按键持续时间最长的键
#
from sbw import *
# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        press=0
        ret=keysPressed[0]
        max_time=0
        for r,c in zip(releaseTimes,keysPressed):
            time=r-press
            if time>max_time or (time==max_time and c>ret):
                max_time=time
                ret=c
            press=r
        return ret
# @lc code=end
assert Solution().slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd")=='c'
