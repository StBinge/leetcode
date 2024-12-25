#
# @lc app=leetcode.cn id=2645 lang=python3
# @lcpr version=30204
#
# [2645] 构造有效字符串的最少插入数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addMinimum(self, word: str) -> int:
        tot=1+sum(x>=y for x,y in pairwise(word))
        return 3*tot - len(word)


# @lc code=end
assert Solution().addMinimum('aaaabb')==9


#
# @lcpr case=start
# "b"\n
# @lcpr case=end

# @lcpr case=start
# "aaa"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

