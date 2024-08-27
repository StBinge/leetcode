#
# @lc app=leetcode.cn id=1893 lang=python3
#
# [1893] 检查是否区域内所有整数都被覆盖
#
from sbw import *


# @lc code=start
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        dif=[0]*52
        for x,y in ranges:
            dif[x]+=1
            dif[y+1]-=1
        for i in range(1,right+1):
            dif[i]=dif[i-1]+dif[i]
        return all(dif[i] for i in range(left,right+1))


# @lc code=end
assert Solution().isCovered([[3,3],[1,1]],3,3)
assert Solution().isCovered([[1, 50]], 1, 50)
assert not Solution().isCovered(ranges=[[1, 10], [10, 20]], left=21, right=21)
assert Solution().isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5)
