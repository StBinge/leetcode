#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#
from sbw import *
# @lc code=start
# import heapq
# import bisect
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N=len(arr)
        if N<2:
            return arr
        for i in range(N-2,-1,-1):
            if arr[i]<=arr[i+1]:
                continue
            j=N-1
            while arr[j]>=arr[i] or arr[j]==arr[j-1]:
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
            break
        return arr



# @lc code=end
assert Solution().prevPermOpt1([3,1,1,3])==[1,3,1,3]
assert Solution().prevPermOpt1([1,9,4,6,7])==[1,7,4,6,9]
assert Solution().prevPermOpt1([1,1,5])==[1,1,5]
assert Solution().prevPermOpt1([3,2,1])==[3,1,2]
