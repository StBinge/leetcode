#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res,level=0,0
        for i,c in enumerate(s):
            if c=='(':
                level+=1
            else:
                level-=1
            if c==')' and s[i-1]=='(':
                res+=1<<(level)
        return res

# @lc code=end
assert Solution().scoreOfParentheses("(()(()))")==6
assert Solution().scoreOfParentheses("()()")==2
assert Solution().scoreOfParentheses("(())")==2
assert Solution().scoreOfParentheses('()')==1
