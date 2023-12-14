#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#
from sbw import *
# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ret=0
        N=len(nums)
        if goal==0:
            cnt=0
            for i in range(N):
                if nums[i]==1:
                    ret+=(cnt+1)*cnt//2
                    cnt=0
                else:
                    cnt+=1
            return ret+(cnt+1)*cnt//2
        l,r=0,1
        s=nums[0]
        while r<N and s<goal:
            s+=nums[r]
            r+=1
        if s<goal:
            return 0
        r-=1
        prev_1=-1
        while r<N:
            nxt_1=r+1
            while nxt_1<N and nums[nxt_1]==0:
                nxt_1+=1
            while l<r and nums[l]==0:
                l+=1
            
            ret+=(l-prev_1)*(nxt_1-r)
            prev_1=l
            r=nxt_1
            l+=1
            
        return ret
# @lc code=end
nums = [0,0,0,0,0]
goal = 0
assert Solution().numSubarraysWithSum(nums,goal)==15

nums = [1,0,1,0,1]
goal = 2
assert Solution().numSubarraysWithSum(nums,goal)==4
