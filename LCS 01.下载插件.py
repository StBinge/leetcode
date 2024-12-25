#
# @lc app=leetcode.cn id=LCS 01 lang=python3
# @lcpr version=30204
#
# [LCS 01] 下载插件
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def leastMinutes(self, n: int) -> int:
        return math.ceil(math.log2(n))+1
# @lc code=end
assert Solution().leastMinutes(4)==3
assert Solution().leastMinutes(2)==2
assert Solution().leastMinutes(1)==1


#
# @lcpr case=start
# 2`>\n
# @lcpr case=end

# @lcpr case=start
# 4`>\n
# @lcpr case=end

#

