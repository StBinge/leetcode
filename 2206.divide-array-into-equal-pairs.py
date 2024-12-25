#
# @lc app=leetcode.cn id=2206 lang=python3
# @lcpr version=30204
#
# [2206] 将数组划分成相等数对
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt=Counter(nums)
        return all( v&1==0 for v in cnt.values())
# @lc code=end



#
# @lcpr case=start
# [3,2,3,2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#

