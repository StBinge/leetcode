#
# @lc app=leetcode.cn id=689 lang=python3
#
# [689] 三个无重叠子数组的最大和
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        L=len(nums)
        s1,s2,s3=sum(nums[:k]),sum(nums[k:2*k]),sum(nums[2*k:3*k])
        max_s1,max_s12,max_total=s1,s1+s2,s1+s2+s3
        max_id1,max_id12=0,(0,k)
        ret=[0,k,2*k]
        for i in range(3*k,L):
            s1=s1-nums[i-3*k]+nums[i-2*k]
            if s1>max_s1:
                max_id1=i-3*k+1
                max_s1=s1

            s2=s2-nums[i-2*k]+nums[i-k]
            if max_s1+s2>max_s12:
                max_id12=(max_id1,i-2*k+1)
                max_s12=max_s1+s2
            s3=s3-nums[i-k]+nums[i]
            if max_s12+s3>max_total:
                max_total=max_s12+s3
                ret=[*max_id12,i-k+1]
        return ret
# @lc code=end
nums=[7,13,20,19,19,2,10,1,1,19]
k=3
assert Solution().maxSumOfThreeSubarrays(nums,k)==[1,4,7]
nums = [1,2,1,2,6,7,5,1]
k = 2
assert Solution().maxSumOfThreeSubarrays(nums,k)==[0,3,5]

nums = [1,2,1,2,1,2,1,2,1]
k = 2
assert Solution().maxSumOfThreeSubarrays(nums,k)==[0,2,4]