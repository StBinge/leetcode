#
# @lc app=leetcode.cn id=1310 lang=python3
#
# [1310] 子数组异或查询
#
from sbw import *
# @lc code=start
import math
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xors=[0]
        for n in arr:
            pre_xors.append(n^pre_xors[-1])
        ret=[]
        for l,r in queries:
            ret.append(pre_xors[r+1]^pre_xors[l])
        return ret
# @lc code=end
assert Solution().xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]])==[8,0,4,4]
assert Solution().xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]])==[2,7,14,8] 
