#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#
from typing import List
# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        L=len(nums)
        if L<3:
            return 0
        nums.sort()
        ret=0
        start=0
        while start<L and nums[start]==0:
            start+=1
        for i in range(start,L):
            k=i+2
            for j in range(i+1,L):
                target=nums[i]+nums[j]
                while k<L and nums[k]<target:
                    k+=1
                ret+=max(k-j-1,0)
        return ret
# @lc code=end
assert Solution().triangleNumber([0,0,0])==0
assert Solution().triangleNumber([2,2,3,4])==3
assert Solution().triangleNumber([4,2,3,4])==4
