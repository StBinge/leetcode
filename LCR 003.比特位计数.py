#
# @lc app=leetcode.cn id=LCR 003 lang=python3
# @lcpr version=30204
#
# [LCR 003] 比特位计数
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ret=[0]
        for i in range(1,n+1):
            ret.append(ret[i>>1]+(i&1))
        return ret
# @lc code=end
assert Solution().countBits(5)==[0,1,1,2,1,2]


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#

