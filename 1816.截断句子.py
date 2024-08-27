#
# @lc app=leetcode.cn id=1816 lang=python3
#
# [1816] 截断句子
#

# @lc code=start
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for i,ch in enumerate(s):
            if ch==' ':
                k-=1
                if k==0:
                    return s[:i]
        return s
# @lc code=end
assert Solution().truncateSentence(s = "Hello how are you Contestant", k = 4)=="Hello how are you"
