#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#
from typing import List
# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ache=
        def dfs(prev,cur):
            if cur in num_pos:
                return 1+dfs(cur,prev+cur)
            else:
                return 0
        ret=0
        num_pos={n:i for i,n in enumerate(arr)}
        for i, n in enumerate(arr):
            def dfs()
# @lc code=end

