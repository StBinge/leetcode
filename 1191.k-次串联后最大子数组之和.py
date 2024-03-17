#
# @lc app=leetcode.cn id=1191 lang=python3
#
# [1191] K 次串联后最大子数组之和
#
from sbw import *
# @lc code=start
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        maxs=0
        s=0
        L=len(arr)
        Mod=10**9+7
        tot=0
        for i in range(2*L if k>1 else L):
            s+=arr[i%L]
            if s<0:
                s=0
            else:
                maxs=max(maxs,s)
            tot+=arr[i%L]
        if k==1 or tot<=0:
            return maxs % Mod
        return (tot//2 * (k-2)+maxs)%Mod
        
# @lc code=end
assert Solution().kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4],5)==20
assert Solution().kConcatenationMaxSum([4,-10,-2,-3,4],1)==4
assert Solution().kConcatenationMaxSum([10000,10000,10000,10000,10000,10000,10000,10000,10000,10000],100000)==999999937
assert Solution().kConcatenationMaxSum(arr = [-1,-2], k = 7)==0
assert Solution().kConcatenationMaxSum(arr = [1,-2,1], k = 5)==2
assert Solution().kConcatenationMaxSum([1,2],3)==9
