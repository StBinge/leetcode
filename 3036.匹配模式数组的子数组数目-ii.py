#
# @lc app=leetcode.cn id=3036 lang=python3
#
# [3036] 匹配模式数组的子数组数目 II
#
from sbw import *
# @lc code=start
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # L=len(nums)
        M=len(pattern)
        pattern.append(2)
        pattern.extend((y>x)-(x>y) for x,y in pairwise(nums))
        L=len(pattern)
        z=[0]*L
        l,r=0,0
        for i in range(1,L):
            if i<=r:
                k=min(z[i-l],r-i+1)
            else:
                k=0

            while i+k<L and pattern[k]==pattern[i+k]:
                k+=1
            z[i]=k
            if z[i]+i>r:
                r=z[i]+i-1
                l=i
        return sum(v==M for v in z) 
# @lc code=end
assert Solution().countMatchingSubarrays([481251768,481251768,481251768,463564806],[0])==2
assert Solution().countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1])==2
assert Solution().countMatchingSubarrays(nums = [1,2,3,4,5,6], pattern = [1,1])==4
