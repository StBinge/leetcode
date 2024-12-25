#
# @lc app=leetcode.cn id=3211 lang=python3
# @lcpr version=30204
#
# [3211] 生成不含相邻零的二进制字符串
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ret = []
        Mask = (1 << n) - 1
        for mask in range(1 << n):
            _mask = Mask ^ mask
            if _mask & (_mask >> 1) == 0:
                ret.append(bin(mask)[2:].rjust(n, "0"))
        return ret


# @lc code=end
assert Solution().validStrings(3) == ["010", "011", "101", "110", "111"]


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
