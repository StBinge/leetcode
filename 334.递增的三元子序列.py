#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
from typing import List
# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N=len(nums)
        if N<3:
            return False
        
        first,sec=nums[0],float('inf')
        for i in range(1,N):
            n=nums[i]
            if n>sec:
                return True
            if n>first:
                sec=n
            else:
                first=n
        return False
    
                
# @lc code=end

assert Solution().increasingTriplet([0,4,1,-1,2])
assert Solution().increasingTriplet([1,5,0,4,1,3])
assert Solution().increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])==False
assert Solution().increasingTriplet([1,2,3,4,5])
assert Solution().increasingTriplet([5,4,3,2,1])==False
assert Solution().increasingTriplet([2,1,5,0,4,6])==True