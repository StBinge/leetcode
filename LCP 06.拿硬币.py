#
# @lc app=leetcode.cn id=LCP 06 lang=python3
# @lcpr version=30204
#
# [LCP 06] 拿硬币
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((c-1)//2+1 for c in coins)
# @lc code=end



#
# @lcpr case=start
# [4,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,10]\n
# @lcpr case=end

#

