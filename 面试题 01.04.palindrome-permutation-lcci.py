#
# @lc app=leetcode.cn id=面试题 01.04 lang=python3
# @lcpr version=30204
#
# [面试题 01.04] 回文排列
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(v&1 for v in Counter(s).values())<2
# @lc code=end
assert Solution().canPermutePalindrome('code')==False


#
# @lcpr case=start
# "tactcoa"\n
# @lcpr case=end

#

