#
# @lc app=leetcode.cn id=2389 lang=python3
# @lcpr version=30204
#
# [2389] 和有限的最长子序列
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        for i in range(len(queries)):
            queries[i]=bisect_right(nums,queries[i])
        return queries
# @lc code=end



#
# @lcpr case=start
# [4,5,2,1]\n[3,10,21]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,5]\n[1]\n
# @lcpr case=end

#

