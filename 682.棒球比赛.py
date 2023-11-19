#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#
from typing import List
# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for op in operations:
            if op=='+':
                stack.append(stack[-1]+stack[-2])
            elif op=='C':
                stack.pop()
            elif op=='D':
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
        return sum(stack)
# @lc code=end

