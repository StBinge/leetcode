#
# @lc app=leetcode.cn id=770 lang=python3
#
# [770] 基本计算器 IV
#
from typing import List
# @lc code=start
class Poly:
    def __init__(self,val:int,vars:dict) -> None:
        self.val=val
        self.vars=vars
    
    def add(self,other:'Poly'):
        self.val+=other.val
        for k,v in other.vars.items():
            self.vars[k]=self.vars.get(k,0)+v

    
    def sub(self,other:'Poly'):
        self.val-=other.val
        for k,v in other.vars.items():
            self.vars[k]=self.vars.get(k,0)-v

    def mul(self,other:'Poly'):
        ret={}
        val=self.val*other.val
        for k2,v2 in other.vars.items():
            v=ret.get(k2,0)+self.val*v2
            ret[k2]=v
        for k1,v1 in self.vars.items():
            v=ret.get(k1,0)+v1*other.val
            ret[k1]=v
            for k2,v2 in other.vars.items():
                kk=tuple(sorted([*k1,*k2]))
                ret[kk]=ret.get(kk,0)+v1*v2
        self.vars=ret
        self.val=val
    
    def to_list(self):
        ret=[]
        keys=sorted(self.vars.keys(),key=lambda k:(-len(k),k))
        for key in keys:
            v=self.vars[key]
            if v==0:
                continue
            ret.append(f'{v}*{"*".join(key)}')
        if self.val:
            ret.append(str(self.val))
        return ret
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        
        varmap={x:y for x,y in zip(evalvars,evalints)}


        def parse(expr:str):
            L=len(expr)
            idx=0
            buckets=[]
            symbols=[]
            # sign=1
            # def make_poly()
            # pair_cnt=0
            while idx<L:
                if expr[idx]=='(':
                    # j=idx+1
                    pair_cnt=1
                    for j in range(idx+1,L):
                        if expr[j]=='(':
                            pair_cnt+=1
                        elif expr[j]==')':
                            pair_cnt-=1
                        if pair_cnt==0:
                            buckets.append(parse(expr[idx+1:j]))
                            idx=j+2
                            break
                    
                elif expr[idx] in '+-*':
                    symbols.append(expr[idx])
                    idx+=2
                    continue
                elif expr[idx].isdigit():
                    num=0
                    while idx<L and expr[idx]!=' ':
                        num=num*10+ord(expr[idx])-ord('0')
                        idx+=1
                    buckets.append(Poly(num,{}))
                    idx+=1
                else:
                    j=idx+1
                    while j<L and expr[j]!=' ':
                        j+=1
                    var=expr[idx:j]
                    if var in varmap:
                        buckets.append(Poly(varmap[var],{}))
                    else:
                        buckets.append(Poly(0,{(var,):1}))
                    idx=j+1
                
                if symbols and symbols[-1]=='*':
                    p2=buckets.pop()
                    p1=buckets.pop()
                    p1.mul(p2)
                    buckets.append(p1)
                    symbols.pop()
            
            ans=buckets[0]
            for i,sy in enumerate(symbols):
                if sy=='+':
                    ans.add(buckets[i+1])
                else:
                    ans.sub(buckets[i+1])
            return ans
        
        p=parse(expression)
        ret= p.to_list()
        return ret



# @lc code=end
expression="((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))"
assert Solution().basicCalculatorIV(expression,[],[])==["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
expression = "(e + 8) * (e - 8)"
evalvars = []
evalints = []
ret=["1*e*e","-64"]
assert Solution().basicCalculatorIV(expression,evalvars,evalints)==ret
expression="a * b * c + b * a * c * 4"
assert Solution().basicCalculatorIV(expression,[],[])==["5*a*b*c"]



expression = "e - 8 + temperature - pressure"

evalvars = ["e", "temperature"]
evalints = [1, 12]
ret=["-1*pressure","5"]

assert Solution().basicCalculatorIV(expression,evalvars,evalints)==ret

expression = "e + 8 - a + 5"
evalvars = ["e"]
evalints = [1]
ret=["-1*a","14"]
assert Solution().basicCalculatorIV(expression,evalvars,evalints)==ret