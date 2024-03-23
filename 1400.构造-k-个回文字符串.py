#
# @lc app=leetcode.cn id=1400 lang=python3
#
# [1400] 构造 K 个回文字符串
#
from sbw import *
# @lc code=start
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        L=len(s)
        if k>L:
            return False
        # if k==L:
        #     return True
        counter=Counter(s)
        odds=sum(v%2 for v in counter.values())
        return odds<=k

# @lc code=end
assert Solution().canConstruct(s = "messi", k = 3)
assert Solution().canConstruct(s = "yzyzyzyzyzyzyzy", k = 2)
assert Solution().canConstruct(s = "true", k = 4)
assert Solution().canConstruct(s = "leetcode", k = 3)==False
assert Solution().canConstruct(s = "annabelle", k = 2)
