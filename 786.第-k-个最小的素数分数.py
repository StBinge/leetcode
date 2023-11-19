#
# @lc app=leetcode.cn id=786 lang=python3
#
# [786] 第 K 个最小的素数分数
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        L=len(arr)
        left,right=0,1
        ri,rj=0,0
        while True:
            dv=0
            mid=(left+right)/2
            cnt=i=0
            for j in range(1,L):
                while True:
                    d=arr[i]/arr[j]
                    if d>mid:
                        break
                    if d>dv:
                        dv=d
                        ri,rj=i,j
                    i+=1
                cnt+=i
            if cnt<k:
                left=mid
            elif cnt==k:
                return [arr[ri],arr[rj]]
            else:
                right=mid

                
# @lc code=end
arr = [1,2,3,5]
k = 3
assert Solution().kthSmallestPrimeFraction(arr,k)==[2,5]
arr = [1,7]
k = 1
assert Solution().kthSmallestPrimeFraction(arr,k)==[1,7]
