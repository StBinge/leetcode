#
# @lc app=leetcode.cn id=LCR 182 lang=python3
# @lcpr version=30204
#
# [LCR 182] 动态口令
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        return password[target:]+password[:target]
# @lc code=end



#
# @lcpr case=start
# "s3cur1tyC0d3"\n4\n
# @lcpr case=end

# @lcpr case=start
# "lrloseumgh"\n6\n
# @lcpr case=end

#

