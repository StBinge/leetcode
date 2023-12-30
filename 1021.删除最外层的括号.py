#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ret=[]
        level=0
        for c in s:
            if c==')':
                level-=1
            if level:
                ret.append(c)
            if c=='(':
                level+=1
        return ''.join(ret)
# @lc code=end
s = "(()())(())(()(()))"
ret="()()()()(())"
assert Solution().removeOuterParentheses(s)==ret

s = "(()())(())"
ret="()()()"
assert Solution().removeOuterParentheses(s)==ret
