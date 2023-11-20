#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
from typing import List
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # def bisect(target,nums:list):
        #     left,right=0,len(nums)
        #     while left<right:
        #         mid=(left+right)//2
        L=len(nums1)
        maps1={}
        for n1 in nums1:
            for n2 in nums2:
                s=n1+n2
                cnt=maps1.get(s,0)+1
                maps1[s]=cnt
        
        maps2={}
        for n3 in nums3:
            for n4 in nums4:
                s=n3+n4
                cnt=maps2.get(s,0)+1
                maps2[s]=cnt

        ret=0
        for s in maps1:
            if -s not in maps2:
                continue
            ret+=maps1[s]*maps2[-s]
        return ret      
# @lc code=end

