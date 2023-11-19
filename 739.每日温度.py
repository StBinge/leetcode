#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ret=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                ret[prev]=i-prev

            stack.append(i)
        return ret
# @lc code=end
temperatures=[89,62,70,58,47,47,46,76,100,70]
ret=[8,1,5,4,3,2,1,1,0,0]
assert Solution().dailyTemperatures(temperatures)==ret

temperatures = [73,74,75,71,69,72,76,73]
ret=[1,1,4,2,1,1,0,0]
assert Solution().dailyTemperatures(temperatures)==ret
temperatures = [30,40,50,60]
ret=[1,1,1,0]
assert Solution().dailyTemperatures(temperatures)==ret
