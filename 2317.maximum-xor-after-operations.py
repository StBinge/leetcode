#
# @lc app=leetcode.cn id=2317 lang=python3
# @lcpr version=30204
#
# [2317] 操作后的最大异或和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x|y,nums)
# @lc code=end
assert Solution().maximumXOR([1,2,3,9,2])==11
assert Solution().maximumXOR([3,2,4,6])==7


#
# @lcpr case=start
# [3,2,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,9,2]\n
# @lcpr case=end

#

