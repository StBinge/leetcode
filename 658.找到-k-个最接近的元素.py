#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#
from typing import List
# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x<=arr[0]:
            return arr[:k]
        L=len(arr)
        if x>=arr[-1]:
            return arr[L-k:]
        if k==L:
            return arr
        left,right=0,L-1
        while left<right:
            mid=(left+right)//2
            if arr[mid]<x:
                left=mid+1
            else:
                right=mid
        left,right=left-1,left
        for _ in range(k):
            if left<0:
                right+=1
            elif right>=L or x-arr[left]<=arr[right]-x:
                left-=1
            else:
                right+=1
        return arr[left+1:left+1+k]

        
# @lc code=end

assert Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9],9,4)==[0,1,1,1,2,3,6,7,8]
assert Solution().findClosestElements([1,2,3,4,5],4,3)==[1,2,3,4]