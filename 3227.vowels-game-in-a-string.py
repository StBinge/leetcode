#
# @lc app=leetcode.cn id=3227 lang=python3
# @lcpr version=30204
#
# [3227] 字符串元音游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(ch in 'aeiou' for ch in s)
        
# @lc code=end



#
# @lcpr case=start
# "leetcoder"\n
# @lcpr case=end

# @lcpr case=start
# "bbcd"\n
# @lcpr case=end

#

