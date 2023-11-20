#
# @lc app=leetcode.cn id=853 lang=python3
#
# [853] 车队
#
from typing import List
# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed=sorted(zip(position,speed))
        time=0
        ret=0
        for p,s in reversed(pos_speed):
            run_time=(target-p)/s
            if run_time>time:
                ret+=1
                time=run_time
        return ret
# @lc code=end
target = 100
position = [0,2,4]
speed = [4,2,1]
assert Solution().carFleet(target,position,speed)==1

target = 10
position = [3]
speed = [3]
ret= 1
assert Solution().carFleet(target,position,speed)==ret

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
assert Solution().carFleet(target,position,speed)==3
