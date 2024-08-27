#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N=len(s1)
        swap=[]
        for i in range(N):
            if s1[i]!=s2[i]:
                swap.append(i)
                if len(swap)>2:
                    return False
        if len(swap)==1:
            return False
        elif len(swap)==0:
            return True
        i,j=swap
        return s1[i]==s2[j] and s2[i]==s1[j]
# @lc code=end
assert Solution().areAlmostEqual(s1 = "kelb", s2 = "kelb")
assert not Solution().areAlmostEqual(s1 = "abcd", s2 = "dcba")
assert not Solution().areAlmostEqual(s1 = "attack", s2 = "defend")
assert Solution().areAlmostEqual(s1 = "bank", s2 = "kanb")
