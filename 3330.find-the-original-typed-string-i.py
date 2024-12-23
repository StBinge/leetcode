#
# @lc app=leetcode.cn id=3330 lang=python3
# @lcpr version=30204
#
# [3330] 找到初始输入字符串 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum(x==y for x,y in pairwise(word))+1
# @lc code=end
assert Solution().possibleStringCount('ere')==1
assert Solution().possibleStringCount('abbcccc')==5


#
# @lcpr case=start
# "abbcccc"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

#

