#
# @lc app=leetcode.cn id=面试题 01.01 lang=python3
# @lcpr version=30204
#
# [面试题 01.01] 判定字符是否唯一
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr))==len(astr)
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

