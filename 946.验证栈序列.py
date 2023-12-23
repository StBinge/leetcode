#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
from sbw import *
# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        pop_i=0
        l1=len(popped)
        for n in pushed:
            stack.append(n)
            while stack and stack[-1]==popped[pop_i]:
                stack.pop()
                pop_i+=1


        return len(stack)==0

# @lc code=end
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
assert Solution().validateStackSequences(pushed,popped)==False

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
assert Solution().validateStackSequences(pushed,popped)
