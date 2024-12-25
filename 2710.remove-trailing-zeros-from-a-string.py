#
# @lc app=leetcode.cn id=2710 lang=python3
# @lcpr version=30204
#
# [2710] 移除字符串中的尾随零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')
# @lc code=end



#
# @lcpr case=start
# "51230100"\n
# @lcpr case=end

# @lcpr case=start
# "123"\n
# @lcpr case=end

#

