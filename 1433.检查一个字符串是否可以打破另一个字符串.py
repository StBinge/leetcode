#
# @lc app=leetcode.cn id=1433 lang=python3
#
# [1433] 检查一个字符串是否可以打破另一个字符串
#
from sbw import *
# @lc code=start
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        c1,c2=Counter(s1),Counter(s2)
        chars=[chr(ord('a')+i) for i in range(26)]
        acc1=list(accumulate(c1[ch] for ch in chars))
        acc2=list(accumulate(c2[ch] for ch in chars))

        return all(a1>=a2 for a1,a2 in zip(acc1,acc2)) or all(a1>=a2 for a1,a2 in zip(acc2,acc1))


# @lc code=end
assert Solution().checkIfCanBreak("szy","cid")
assert Solution().checkIfCanBreak(s1 = "leetcodee", s2 = "interview")
assert Solution().checkIfCanBreak(s1 = "abe", s2 = "acd")==False
assert Solution().checkIfCanBreak(s1 = "abc", s2 = "xya")
