#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#
from sbw import *
# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ret=[]
        dif=10**7
        for i in range(1,len(arr)):
            d=arr[i]-arr[i-1]
            if d<dif:
                dif=d
                ret=[[arr[i-1],arr[i]]]
            elif d==dif:
                ret.append([arr[i-1],arr[i]])
        return ret
# @lc code=end
assert Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27])==[[-14,-10],[19,23],[23,27]]
