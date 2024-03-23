#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        zero=int(s[0]=='0')
        ones=s[1:].count('1')
        ret=zero+ones
        for c in s[1:-1]:
            if c=='0':
                zero+=1
                ret=max(ret,zero+ones)
            else:
                ones-=1
        return ret
# @lc code=end
assert Solution().maxScore('1111')==3
assert Solution().maxScore('00111')==5
assert Solution().maxScore('011101')==5
