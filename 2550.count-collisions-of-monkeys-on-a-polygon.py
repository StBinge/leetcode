#
# @lc app=leetcode.cn id=2550 lang=python3
# @lcpr version=30204
#
# [2550] 猴子碰撞的方法数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2,n,10**9+7)-2)%(10**9+7)
# @lc code=end
assert Solution().monkeyMove(500000003)==1000000006


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

