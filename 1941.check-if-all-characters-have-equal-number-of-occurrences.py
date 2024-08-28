#
# @lc app=leetcode.cn id=1941 lang=python3
# @lcpr version=30204
#
# [1941] 检查是否所有字符出现次数相同
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return all(x==y for x,y in pairwise(Counter(s).values()))
# @lc code=end



#
# @lcpr case=start
# "abacbc"\n
# @lcpr case=end

# @lcpr case=start
# "aaabb"\n
# @lcpr case=end

#

