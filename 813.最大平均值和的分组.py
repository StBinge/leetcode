#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#
from typing import List
# @lc code=start
import itertools
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        l=len(nums)
        prefix=list(itertools.accumulate(nums,initial=0 ))
        f=[0]*(l+1)
        for i in range(1,l+1):
            f[i]=prefix[i]/i
        
        for j in range(2,k+1):
            for i in range(l,j-1,-1):
                for x in range(j-1,i):
                    f[i]=max(f[i],f[x]+(prefix[i]-prefix[x])/(i-x))
        return f[-1]
# @lc code=end
nums = [9,1,2,3,9]
k = 3
assert Solution().largestSumOfAverages(nums,k)==20