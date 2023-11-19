#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
from typing import List
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # left=right=0
        # sum=nums[0]
        # L=len(nums)
        # while right<
        # presums=[0]
        presum=0
        counter={0:1}
        ret=0
        for n in nums:
            presum+=n
            ret+=counter.get(presum-k,0)
            cnt=counter.get(presum,0)+1
            counter[presum]=cnt
        return ret
        

# @lc code=end
assert Solution().subarraySum([1,1,1],2)==2
assert Solution().subarraySum([1,2,3],3)==2
