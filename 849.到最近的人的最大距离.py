#
# @lc app=leetcode.cn id=849 lang=python3
#
# [849] 到最近的人的最大距离
#
from typing import List
# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n=len(seats)
        ret=0
        left=0
        while seats[left]==0:
            left+=1
        ret=left
        
        while left<n:
            while left+1< n and  seats[left+1]==1:
                left+=1
            right=left+1
            while right<n and seats[right]==0:
                right+=1
            if right==n:
                ret=max(ret,n-left-1)
            else:
                ret=max(ret,(right-left)//2)
            left=right
        return ret
# @lc code=end
assert Solution().maxDistToClosest([1,0,0,0])==3
seats = [1,0,0,0,1,0,1]
assert Solution().maxDistToClosest(seats)==2
