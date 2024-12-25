#
# @lc app=leetcode.cn id=2592 lang=python3
# @lcpr version=30204
#
# [2592] 最大化数组的伟大值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        return len(nums)-max(cnt.values())

# @lc code=end
assert Solution().maximizeGreatness([1,3,5,2,1,3,1])==4


#
# @lcpr case=start
# [1,3,5,2,1,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#

