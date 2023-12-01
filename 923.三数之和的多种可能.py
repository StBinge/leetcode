#
# @lc app=leetcode.cn id=923 lang=python3
#
# [923] 三数之和的多种可能
#
from sbw import *
# @lc code=start
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ret=0
        Mod=10**9+7
        counters=Cou
        arr.sort()
        for i,n in enumerate(arr)
        
# @lc code=end
arr = [1,1,2,2,2,2]
target = 5
ret=12
assert Solution().threeSumMulti(arr,target)==12

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
ret=20
assert Solution().threeSumMulti(arr,target)==20
