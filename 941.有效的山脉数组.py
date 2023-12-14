#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#
from numpy import False_
from sbw import *
# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        peek=-1
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                continue
            else:
                peek=i-1
                break
        if peek<=0:
            return False
        for i in range(peek,len(arr)-1):
            if arr[i]>arr[i+1]:
                continue
            else:
                return False
        return True
# @lc code=end

assert Solution().validMountainArray([9,8,7,6,5,4,3,2,1,0])==False
assert Solution().validMountainArray([0,3,2,1])==True
assert Solution().validMountainArray([3,5,5])==False
assert Solution().validMountainArray([2,1])==False