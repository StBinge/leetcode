#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#
from typing import List
# @lc code=start
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        L=len(nums)
        if L<2:
            return False
        s=sum(nums)
        m=L//2
        if all((s*i)%L for i in range(1,m+1)):
            return False
        
        f=[set() for _ in range(m+1)]
        f[0].add(0)
        for n in nums:
            for i in range(m,0,-1):
                for x in f[i-1]:
                    cur=x+n
                    if cur*L==i*s:
                        return True
                    f[i].add(cur)
        return False

# @lc code=end
nums=[5,3,11,19,2]
assert Solution().splitArraySameAverage(nums)

assert Solution().splitArraySameAverage([1,3])==False
nums = [1,2,3,4,5,6,7,8]
assert Solution().splitArraySameAverage(nums)
