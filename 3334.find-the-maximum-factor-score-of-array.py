#
# @lc app=leetcode.cn id=3334 lang=python3
# @lcpr version=30204
#
# [3334] 数组的最大因子得分
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N=len(nums)
        if N==1:
            return nums[0]**2
        suf_gcd=[nums[-1]]*N
        suf_lcm=[nums[-1]]*N
        for i in range(N-2,-1,-1):
            suf_gcd[i]=math.gcd(nums[i],suf_gcd[i+1])
            suf_lcm[i]=math.lcm(nums[i],suf_lcm[i+1])

        ret=max(suf_gcd[1]*suf_lcm[1],suf_gcd[0]*suf_lcm[0])
        pre_gcd=nums[0]
        pre_lcm=nums[0]
        for i in range(1,N-1):
            ret=max(ret,math.gcd(pre_gcd,suf_gcd[i+1])*math.lcm(pre_lcm,suf_lcm[i+1]))
            pre_gcd=math.gcd(pre_gcd,nums[i])
            pre_lcm=math.lcm(pre_lcm,nums[i])
        
        return max(ret,pre_gcd*pre_lcm)
            
# @lc code=end

assert Solution().maxScore([10,25,6])==250
assert Solution().maxScore( [3])==9
assert Solution().maxScore( [1,2,3,4,5])==60
assert Solution().maxScore([2,4,8,16])==64

#
# @lcpr case=start
# [2,4,8,16]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [3]\n
# @lcpr case=end

#

