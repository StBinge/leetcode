#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#
from sbw import *
# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key=lambda x:x[0]-x[1])
        N=len(costs)//2
        return sum(a for a,_ in costs[:N])+sum(b for _,b in costs[N:])
# @lc code=end
costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
assert Solution().twoCitySchedCost(costs)==3086

costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
assert Solution().twoCitySchedCost(costs)==1859

costs = [[10,20],[30,200],[400,50],[30,20]]
assert Solution().twoCitySchedCost(costs)==110
