#
# @lc app=leetcode.cn id=面试题 01.02 lang=python3
# @lcpr version=30204
#
# [面试题 01.02] 判定是否互为字符重排
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1)==Counter(s2)
# @lc code=end



#
# @lcpr case=start
# "abc"\n"bca"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"bad"\n
# @lcpr case=end

#

