#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#
from sbw import *
# @lc code=start
import bisect
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        span=len(arr)//4+1
        for i in range(0,len(arr),span):
            left=bisect.bisect_left(arr,arr[i],hi=i)
            right=bisect.bisect_right(arr,arr[i],lo=i)
            if right-left>=span:
                return arr[i]
        
# @lc code=end
assert Solution().findSpecialInteger([1])==1
assert Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10])==6
