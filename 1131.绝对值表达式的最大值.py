#
# @lc app=leetcode.cn id=1131 lang=python3
#
# [1131] 绝对值表达式的最大值
#
from sbw import *


# @lc code=start
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        s=[[] for _ in range(4)]
        for i,[x,y] in enumerate(zip(arr1,arr2)):
            s[0].append(x+y+i)
            s[1].append(x+y-i)
            s[2].append(x-y-i)
            s[3].append(x-y+i)
        ret=0
        for nums in s:
            ret=max(ret,max(nums)-min(nums))
        return ret
# @lc code=end
assert Solution().maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]) == 20
assert Solution().maxAbsValExpr(arr1=[1, 2, 3, 4], arr2=[-1, 4, 5, 6]) == 13

