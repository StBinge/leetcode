#
# @lc app=leetcode.cn id=LCR 169 lang=python3
# @lcpr version=30204
#
# [LCR 169] 招式拆解 II
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dismantlingAction(self, arr: str) -> str:
        cnt=Counter(arr)
        for ch in arr:
            if cnt[ch]==1:
                return ch
        return ' '
# @lc code=end



#
# @lcpr case=start
# "abbccdeff"\n
# @lcpr case=end

# @lcpr case=start
# "ccdd"\n
# @lcpr case=end

#

