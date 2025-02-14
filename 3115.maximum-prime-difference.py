#
# @lc app=leetcode.cn id=3115 lang=python3
# @lcpr version=30204
#
# [3115] 质数的最大距离
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
        N=len(nums)
        for i in range(N):
            if nums[i] in primes:
                for j in range(N-1,-1,-1):
                    if nums[j] in primes:
                        return j-i
# @lc code=end
assert Solution().maximumPrimeDifference([93,43,62,91])==0
assert Solution().maximumPrimeDifference([51,97,78,37])==2
assert Solution().maximumPrimeDifference([37,34,97,57])==2
assert Solution().maximumPrimeDifference([71,87,49])==0


#
# @lcpr case=start
# [4,2,9,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,8,2,8]\n
# @lcpr case=end

#

