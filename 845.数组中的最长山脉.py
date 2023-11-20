#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#
from typing import List
# @lc code=start
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)
        left=0
        ret=0
        while left<n:
            right=left+1
            while right<n and arr[right]>arr[right-1]:
                right+=1
            if right==n:
                break
            if right==left+1 or arr[right]==arr[right-1]:
                left=right
                continue
            while right<n and arr[right]<arr[right-1]:
                right+=1
            ret=max(ret,right-left)
            left=right-1
        return ret


assert Solution().longestMountain([3,3,1])==0
assert Solution().longestMountain([0,1,2,3,4,5,4,3,2,1,0])==11
assert Solution().longestMountain([2,1,4,7,3,2,5])==5
assert Solution().longestMountain([2,2,2])==0