#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
from typing import List
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i1,i2=0,0
        l1,l2=len(nums1),len(nums2)
        ret=[]
        while i1<l1 and i2<l2:
            n1=nums1[i1]
            n2=nums2[i2]
            if n1==n2:
                if not ret or n1!=ret[-1]:
                    ret.append(n1)
                i1+=1
                i2+=1
            elif n1<n2:
                i1+=1
            else:
                i2+=1
        return ret

# @lc code=end

