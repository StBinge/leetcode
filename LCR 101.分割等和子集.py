#
# @lc app=leetcode.cn id=LCR 101 lang=python3
# @lcpr version=30204
#
# [LCR 101] 分割等和子集
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s&1:
            return False
        target=s//2
        if max(nums)>target:
            return False
        f=[False]*(target+1)
        f[0]=True
        for n in nums:
            for t in range(target,n-1,-1):
                f[t]|=f[t-n]
            if f[target]:
                return True
        return False
# @lc code=end
assert Solution().canPartition([1,3,4,4])==False
assert Solution().canPartition([1,2,3,5])==False
assert Solution().canPartition([1,5,11,5])


#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

