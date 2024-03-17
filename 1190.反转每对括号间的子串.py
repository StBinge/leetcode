#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        L=len(s)
        pairs=[-1]*L
        stack=[]
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            elif c==')':
                p=stack.pop()
                pairs[p]=i
                pairs[i]=p
        
        idx=0
        step=1
        ret=[]
        while idx<L:
            c=s[idx]
            if c=='(' or c==')':
                idx=pairs[idx]
                step*=-1
            else:
                ret.append(c)
            idx+=step
        return ''.join(ret)
# @lc code=end
assert Solution().reverseParentheses("(u(love)i)")=='iloveu'
assert Solution().reverseParentheses("(abcd)")=='dcba'
