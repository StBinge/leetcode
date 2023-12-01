#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#
from typing import List
# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        left,right=0,n-2
        ret=0
        while left<=right:
            mid=(left+right)//2
            if arr[mid]>arr[mid+1]:
                ret=mid
                right=mid-1
            else:
                left=mid+1
        return ret
# @lc code=end
assert Solution().peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19])==2
assert Solution().peakIndexInMountainArray([0,1,0])==1
assert Solution().peakIndexInMountainArray([0,2,1,0])==1
assert Solution().peakIndexInMountainArray([0,10,5,2])==1
