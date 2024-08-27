#
# @lc app=leetcode.cn id=1674 lang=python3
#
# [1674] 使数组互补的最少操作次数
#
from sbw import *
# @lc code=start
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N=len(nums)
        dif=[0]*(2*limit+2)
        for i in range(N//2):
            a,b=nums[i],nums[N-1-i]
            s=a+b
            mi=1+min(a,b)
            ma=limit+max(a,b)
            dif[mi]-=1
            dif[ma+1]+=1
            dif[s]-=1
            dif[s+1]+=1
        res=N
        s=N
        for x in dif[2:-1]:
            s+=x
            res=min(s,res)
        return res

# @lc code=end
assert Solution().minMoves(nums = [1,2,4,3], limit = 4)==1
