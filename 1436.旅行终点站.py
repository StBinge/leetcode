#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#
from sbw import *
# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts=set(path[0] for path in paths)
        for _,e in paths:
            if e not in starts:
                return e
# @lc code=end

