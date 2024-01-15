#
# @lc app=leetcode.cn id=1096 lang=python3
#
# [1096] 花括号展开 II
#
from sbw import *
# @lc code=start
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        L=len(expression)
        idx=0
        set_stack=[]
        op_stack=[]

        def product():
            right=set_stack.pop()
            left=set_stack.pop()
            ret=set()
            for a in left:
                for b in right:
                    ret.add(a+b)
            set_stack.append(ret)

        def union():
            right=set_stack.pop()
            left=set_stack.pop()
            left.update(right)
            set_stack.append(left)
        
        while idx<L:
            char=expression[idx]
            if char=='{':
                if idx>0 and (expression[idx-1]=='}' or expression[idx-1].isalpha()):
                    op_stack.append('*')
                op_stack.append('{')
            elif char=='}':
                while op_stack[-1]!='{':
                    op=op_stack.pop()
                    if op=='+':
                        union()
                    else:
                        product()
                op_stack.pop()
            elif char==',':
                while op_stack and op_stack[-1]=='*':
                    op_stack.pop()
                    product()
                op_stack.append('+')
            else:
                if idx> 0 and expression[idx-1]=='}':
                    op_stack.append('*')
                chars=[]
                while idx<L and expression[idx].isalpha():
                    chars.append(expression[idx])
                    idx+=1
                set_stack.append({''.join(chars)})
                idx-=1
            idx+=1
        while op_stack:
            op=op_stack.pop()
            if op=='*':
                product()
            else:
                union()
        return sorted(set_stack[0])
# @lc code=end
ret=Solution().braceExpansionII(expression = "{{a,z},a{b,c},{ab,z}}")
assert ret==["a","ab","ac","z"]
ret=Solution().braceExpansionII(expression = "{a,b}c{d,e}f")
assert ret==["acdf","acef","bcdf","bcef"]
ret=Solution().braceExpansionII(expression = "{a,b}{c,{d,e}}")
assert ret==["ac","ad","ae","bc","bd","be"]
