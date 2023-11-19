#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
from typing import List
# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        inf=float('-inf')
        m1=m2=m3=inf
        for n in nums:
            if n>m1:
                m1,m2,m3=n,m1,m2
            elif n==m1:
                continue
            elif n>m2:
                m2,m3=n,m2
            elif n==m2:
                continue
            elif n>m3:
                m3=n
        
        if m3>-2**31-1:
            return m3
        else:
            return m1
    
            

# @lc code=end

assert Solution().thirdMax([1,1,2])==2
assert Solution().thirdMax([3,2,1])==1
assert Solution().thirdMax([1,2])==2
assert Solution().thirdMax([2,2,3,1])==1