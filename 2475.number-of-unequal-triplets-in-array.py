#
# @lc app=leetcode.cn id=2475 lang=python3
# @lcpr version=30204
#
# [2475] 数组中不等三元组的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        N=len(nums)
        pre=ret=0
        for v in cnt.values():
            ret+=pre*v*(N-pre-v)
            pre+=v
        return ret
# @lc code=end
assert Solution().unequalTriplets([1,1,1,1,1])==0

assert Solution().unequalTriplets([4,4,2,4,3])==3

#
# @lcpr case=start
# [4,4,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n
# @lcpr case=end

#

