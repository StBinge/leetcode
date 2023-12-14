#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#
from sbw import *
# @lc code=start
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ret=[]
        for n in range(len(arr),0,-1):
            idx=0
            for i in range(1,n):
                if arr[i]>arr[idx]:
                    idx=i
            if idx==n-1:
                continue
            l,r=0,idx
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            l,r=0,n-1
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            ret.append(idx+1)
            ret.append(n)
        return ret
            
# @lc code=end
arr=[3,2,4,1]
ret=[4,2,4,3]
assert Solution().pancakeSort(arr)==ret