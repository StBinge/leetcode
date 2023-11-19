#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 小行星碰撞
#
from typing import List
# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for n in asteroids:
            if n<0:
                hold=True
                while stack and stack[-1]>0:
                    pre=stack.pop()
                    if pre>-n:
                        stack.append(pre)
                        hold=False
                        break
                    elif pre==-n:
                        hold=False
                        break
                if hold:
                    stack.append(n)
            else:
                stack.append(n)
        return stack
# @lc code=end
assert Solution().asteroidCollision([5,10,-5])==[5,10]
assert Solution().asteroidCollision([8,-8])==[]
