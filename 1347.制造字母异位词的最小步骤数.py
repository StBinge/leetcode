#
# @lc app=leetcode.cn id=1347 lang=python3
#
# [1347] 制造字母异位词的最小步骤数
#
from sbw import *
# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter=Counter(s)
        for c in t:
            if c in s:
                counter[c]-=1
        ret=0
        for v in counter.values():
            if v>0:
                ret+=v
        return ret
# @lc code=end
assert Solution().minSteps(s = "friend", t = "family")==4
assert Solution().minSteps(s = "leetcode", t = "practice")==5
assert Solution().minSteps(s = "bab", t = "aba")==1
