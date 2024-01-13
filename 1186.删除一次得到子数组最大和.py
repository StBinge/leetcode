#
# @lc app=leetcode.cn id=1186 lang=python3
#
# [1186] 删除一次得到子数组最大和
#
from sbw import *
# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        L=len(arr)

        # Min=float('-inf')

        f0,f1=arr[0],0
        # ma=arr[0]
        ret=arr[0]
        for i in range(1,L):
            f0,f1=max(arr[i],f0+arr[i]),max(f0,f1+arr[i])
            ret=max(ret,f0,f1)
        return ret
    

# @lc code=end
assert Solution().maximumSum([-50])==-50
assert Solution().maximumSum([2,1,-2,-5,-2])==3
assert Solution().maximumSum([2,1,-2,-5,-2])==3
assert Solution().maximumSum(arr = [1,-2,-2,3])==3
assert Solution().maximumSum(arr = [1,-2,0,3])==4
