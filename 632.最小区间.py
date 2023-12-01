#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        Min,Max=float('inf'),float('-inf')
        idx_map={}
        L=len(nums)
        for i,vec in enumerate(nums):
            for x in vec:
                Min=min(Min,x)
                Max=max(Max,x)
                rows=idx_map.setdefault(x,[])
                rows.append(i)
        best_left,best_right=Min,Max
        left,right=Min,Min
        freq=[0]*L
        fit=0
        while right<=Max:
            if right in idx_map:
                for rid in idx_map[right]:
                    freq[rid]+=1
                    if freq[rid]==1:
                        fit+=1
            while fit==L:
                if right-left<best_right-best_left:
                    best_left=left
                    best_right=right
                if left in idx_map:
                    for rid in idx_map[left]:
                        freq[rid]-=1
                        if freq[rid]==0:
                            fit-=1
                left+=1
            right+=1
        return [best_left,best_right]

# @lc code=end
nums = [[-5,-4,-3,-2,-1],[1,2,3,4,5]]
assert Solution().smallestRange(nums)==[-1,1]
nums = [[1,2,3],[1,2,3],[1,2,3]]
assert Solution().smallestRange(nums)==[1,1]
nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
assert Solution().smallestRange(nums)==[20,24]