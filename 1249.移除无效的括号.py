#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # left=0
        deleted=[]
        stack=[]
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            elif c==')':
                if stack:
                    stack.pop()
                else:
                    deleted.append(i)
        d=set(deleted+stack)
        ret=[s[i] for i in range(len(s)) if i not in d]
        return ''.join(ret)
# @lc code=end
assert Solution().minRemoveToMakeValid("))((")==""
assert Solution().minRemoveToMakeValid("a)b(c)d")=="ab(c)d"
assert Solution().minRemoveToMakeValid("lee(t(c)o)de)")=="lee(t(c)o)de"
