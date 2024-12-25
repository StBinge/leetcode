#
# @lc app=leetcode.cn id=2138 lang=python3
# @lcpr version=30204
#
# [2138] 将字符串拆分为若干长度为 k 的组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        for i in range(0, len(s), k):
            ret.append(s[i : i + k])
        if len(ret[-1]) != k:
            ret[-1] = ret[-1].ljust(k, fill)
        return ret


# @lc code=end
assert Solution().divideString(s="abcdefghi", k=3, fill="x") == ["abc", "def", "ghi"]


#
# @lcpr case=start
# "abcdefghi"\n3\n"x"\n
# @lcpr case=end

# @lcpr case=start
# "abcdefghij"\n3\n"x"\n
# @lcpr case=end

#
