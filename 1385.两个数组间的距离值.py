#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#
from sbw import *
# @lc code=start

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        L=len(arr2)
        ret=0
        for n in arr1:
            idx=bisect_right(arr2,n)
            if idx>0 and (n-arr2[idx-1])<=d:
                continue
            if idx<L and (arr2[idx]-n)<=d:
                continue
            ret+=1
        return ret
# @lc code=end
assert Solution().findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6)==1
assert Solution().findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3)==2
assert Solution().findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2)==2
