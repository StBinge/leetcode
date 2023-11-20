#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
from typing import List
# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        L1,L2=len(nums1),len(nums2)
        base=101
        mod=10**9+9
        def check(length):
            nonlocal L1,L2
            hash1=0            
            for i in range(length):
                hash1=(hash1*base+nums1[i])%mod
            set1={hash1}
            mul=pow(base,length-1,mod)
            for i in range(length,L1):
                hash1=((hash1-mul*nums1[i-length])*base + nums1[i])%mod
                set1.add(hash1)
            hash2=0
            for i in range(length):
                hash2=(hash2*base+nums2[i])%mod
            if hash2 in set1:
                return True
            for i in range(length,L2):
                hash2=((hash2-nums2[i-length]*mul)*base+nums2[i])%mod
                if hash2 in set1:
                    return True
            return False
        left,right=0,min(L1,L2)
        ans=0
        while left<=right:
            mid=(left+right)//2
            if check(mid):
                left=mid+1
                ans=mid
            else:
                right=mid-1
        return ans
# @lc code=end
nums1=[1,0,0,0,1]
nums2=[1,0,0,1,1]
assert Solution().findLength(nums1,nums2)==3

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
assert Solution().findLength(nums1,nums2)==3
nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
assert Solution().findLength(nums1,nums2)==5