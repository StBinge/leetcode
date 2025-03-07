#
# @lc app=leetcode.cn id=2735 lang=python3
# @lcpr version=30204
#
# [2735] 收集巧克力
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        N=len(nums)
        s=sum(nums)
        mi=min(nums)
        D=s-mi*N
        mx_rotation=D//x
        ret=cur=s
        for i in range(mx_rotation):
            cur+=x
            n0=nums[0]
            for i in range(N-1):
                mi=min(nums[i],nums[i+1])
                cur-=nums[i]-mi
                nums[i]=mi
            mi=min(n0,nums[-1])
            cur-=nums[-1]-mi
            nums[-1]=mi
            ret=min(ret,cur)
        return ret
# @lc code=end
assert Solution().minCost([31,25,18,59],27)==119
assert Solution().minCost(nums = [1,2,3], x = 4)==6
assert Solution().minCost(nums = [20,1,15], x = 5)==13


#
# @lcpr case=start
# [20,1,15]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n4\n
# @lcpr case=end

#

