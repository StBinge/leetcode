#
# @lc app=leetcode.cn id=1414 lang=python3
#
# [1414] 和为 K 的最少斐波那契数字数目
#
from sbw import *
# @lc code=start
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # if k==1:
        #     return 1
        nums=[1,1]


        while nums[-1]<=k:
            nums.append(nums[-1]+nums[-2])
        
        ans=0
        i=len(nums)-1
        while k>0:
            if k>=nums[i]:
                k-=nums[i]
                ans+=1
            i-=1
        return ans



# @lc code=end
assert Solution().findMinFibonacciNumbers(19)==3
assert Solution().findMinFibonacciNumbers(10)==2
assert Solution().findMinFibonacciNumbers(7)==2
