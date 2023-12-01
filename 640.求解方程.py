#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        left,right=equation.split('=')
        def parse(s:str):
            x_cnt=0
            val_cnt=0
            idx=0
            L=len(s)
            sign=1
            cur_val=0
            while idx<L:
                if s[idx] in '+-':
                    val_cnt+=cur_val*sign
                    cur_val=0
                    sign=-1 if s[idx]=='-' else 1
                    idx+=1
                elif s[idx] =='x':
                    if idx>0 and s[idx-1].isnumeric():
                        x_cnt+=cur_val*sign
                    else:
                        x_cnt+=1*sign
                    cur_val=0
                    idx+=1
                else:  
                    while idx<L and s[idx].isnumeric():
                        cur_val=cur_val*10 +ord(s[idx])-ord('0')
                        idx+=1
 
            return x_cnt,val_cnt+cur_val*sign
        
        left_x,left_v=parse(left)
        right_x,right_v=parse(right)
        x=left_x-right_x
        val=right_v-left_v
        if x==0 and val==0:
            return "Infinite solutions"
        if x==0 and val or val%x:
            return "No solution"
        
        return 'x='+str(val//x)
# @lc code=end

assert Solution().solveEquation("x+5-3+x=6+x-2")=="x=2"
assert Solution().solveEquation("x=x")=="Infinite solutions"
assert Solution().solveEquation("0x=0")=="Infinite solutions"
assert Solution().solveEquation("2x=x")=="x=0"
assert Solution().solveEquation("2x=1")=="No solution"
assert Solution().solveEquation("x=x+2")=="No solution"