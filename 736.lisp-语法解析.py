#
# @lc app=leetcode.cn id=736 lang=python3
#
# [736] Lisp 语法解析
#

# @lc code=start
class Solution:
    def evaluate(self, expression: str) -> int:
        global_vals={}

        # L=len(expression)
        idx=0

        def parse_var_name():
            nonlocal idx
            start=idx
            while expression[idx]!=' ' and expression[idx]!=')':
                idx+=1
            return expression[start:idx]

        def parse_val():
            nonlocal idx
            sign=1
            if expression[idx]=='-':
                sign=-1
                idx+=1
            num=0
            while expression[idx]!=' ' and expression[idx]!=')':
                num=num*10+ord(expression[idx])-ord('0')
                idx+=1
            return num*sign
        
        def parse_let():
            nonlocal idx
            # var_name=''
            ret=None
            vars=[]
            while True:
                if expression[idx].islower()==False:
                    ret=parse()
                    break

                var_name=parse_var_name()
                if expression[idx]==')':
                    ret=global_vals[var_name][-1]
                    break

                idx+=1
                
                global_vals.setdefault(var_name,[]).append(parse())
                vars.append(var_name)
                idx+=1
            for var in vars:
                global_vals[var].pop()
            return ret
                
        
        Add=lambda x,y:x+y
        Mul=lambda x,y:x*y
        def parse_calc(operator):
            nonlocal idx
            val1=parse()
            idx+=1
            val2=parse()
            
            return operator(val1,val2)


                    
        def parse():
            nonlocal idx
            if expression[idx]!='(':
                if expression[idx].islower():
                    return global_vals[parse_var_name()][-1]
                return parse_val()
            idx+=1
            if expression[idx]=='l':
                idx+=4
                ret= parse_let()
            elif expression[idx]=='a':
                idx+=4
                ret= parse_calc(Add)
            else:
                idx+=5
                ret= parse_calc(Mul)
            idx+=1
            return ret
        
        return parse()
                


# @lc code=end
expression="(let x 2 (add (let x 3 (let x 4 x)) x))"
assert Solution().evaluate(expression)==6

expression = "(let var 78 b 77 (let c 33 (add c (mult var 66))))"
assert Solution().evaluate(expression)==5181
expression = "(let x -2 y x y)"
assert Solution().evaluate(expression)==-2
expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
assert Solution().evaluate(expression)==14

expression="(let x 7 -12)"
assert Solution().evaluate(expression)==-12

expression="(add 1 2)"
assert Solution().evaluate(expression)==3
expression="(let a1 3 b2 (add a1 1) b2)"
assert Solution().evaluate(expression)==4

expression = "(let x 3 x 2 x)"
assert Solution().evaluate(expression)==2
expression = "(let x 1 y 2 x (add x y) (add x y))"
assert Solution().evaluate(expression)==5
