#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        L=len(expression)
        stack=[]
        idx=0

        

        for ch in expression:
            if ch==',':
                continue
            if ch ==')':
                t=f=0
                while stack[-1]!='(':
                    c=stack.pop()
                    if c=='t':
                        t+=1
                    else:
                        f+=1
                stack.pop()
                op=stack.pop()
                if op=='!':
                    stack.append('f' if t==1 else 't')
                elif op=='&':
                    stack.append('t' if f==0 else 'f')
                else:
                    stack.append('t' if t>0 else 'f')
            else:
                stack.append(ch)

        return True if stack[0]=='t' else False
# @lc code=end
assert Solution().parseBoolExpr("!(&(f,t))") == True
assert Solution().parseBoolExpr("|(f,f,f,t)") == True
assert Solution().parseBoolExpr("&(|(f))") == False
