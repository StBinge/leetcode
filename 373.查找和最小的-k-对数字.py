#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        L1,L2=len(nums1),len(nums2)
        left=nums1[0]+nums2[0]
        right=nums1[-1]+nums2[-1]+1

        while left<right:
            mid=(left+right)//2
            cnt=0
            i,j=0,L2-1
            while i<L1 and j>-1:
                if nums1[i]+nums2[j]>mid:
                    j-=1
                else:
                    cnt+=j+1
                    i+=1
            if cnt>=k:
                right=mid
            elif cnt<k:
                left=mid+1
        pair_sum=left
        ret=[]
        j=L2-1
        for n1 in nums1:
            while j>=0 and n1+nums2[j]>=pair_sum:
                j-=1
            for jj in range(j+1):
                ret.append([n1,nums2[jj]])
                if len(ret)==k:
                    return ret
        
        j=L2-1
        for n1 in nums1:
            while j>=0 and n1+nums2[j]>pair_sum:
                j-=1
            jj=j
            while jj>=0 and n1+nums2[jj]==pair_sum:
                ret.append([n1,nums2[jj]])
                if len(ret)==k:
                    return ret
                jj-=1
        return ret
# @lc code=end
nums1 = [1,2]
nums2 = [3]
k = 3 
print(Solution().kSmallestPairs(nums1,nums2,k))
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(Solution().kSmallestPairs(nums1,nums2,k))

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(Solution().kSmallestPairs(nums1,nums2,k))


nums1 = [1,2,3]
nums2 = [1,1,2]
k = 10
print(Solution().kSmallestPairs(nums1,nums2,k))
