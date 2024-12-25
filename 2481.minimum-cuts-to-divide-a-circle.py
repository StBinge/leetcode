#
# @lc app=leetcode.cn id=2481 lang=python3
# @lcpr version=30204
#
# [2481] 分割圆的最少切割次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n==1:
            return 0
        if n&1:
            return n
        return n//2

        
# @lc code=end
assert Solution().numberOfCuts(4)==2


#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

