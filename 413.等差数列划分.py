#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#
from typing import List
# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        N=len(nums)
        if N<3:
            return 0
        # dif=[0]*(N-1)
        # for i in range(N-1):
        #     dif[i]=nums[i]-nums[i+1]
        ret=0
        dif=nums[1]-nums[0]
        cnt=0
        for i in range(2,N):
            cur=nums[i]-nums[i-1]
            if cur==dif:
                cnt+=1
            else:
                dif=cur
                cnt=0
            ret+=cnt
        # if cnt>=2:
        #     ret+=(cnt*(cnt-1))//2
        return ret


# @lc code=end

assert Solution().numberOfArithmeticSlices([1,2,3,8,9,10])==2
assert Solution().numberOfArithmeticSlices([1,2,3])==1
assert Solution().numberOfArithmeticSlices([1,2,3,4])==3
assert Solution().numberOfArithmeticSlices([1])==0