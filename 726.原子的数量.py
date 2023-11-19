#
# @lc app=leetcode.cn id=726 lang=python3
#
# [726] 原子的数量
#

# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counter={}

        L=len(formula)
        # stack=[]
        # cur=stack[-1]

        idx=L-1
        mul_stack=[1]
        # cur_mul=1
        num=1
        while idx>=0:
            if formula[idx]==')':
                mul_stack.append(num*mul_stack[-1])
                # cur_mul=mul_stack[-1]
                num=1
                idx-=1
            elif formula[idx]=='(':
                mul_stack.pop()
                # cur_mul=mul_stack[-1]
                idx-=1
            elif formula[idx].isnumeric():
                end=idx
                while idx>=0 and formula[idx].isnumeric():
                    idx-=1
                start=idx+1
                num=int(formula[start:end+1])
            else:
                end=idx

                while idx>=0 and formula[idx].islower():
                    idx-=1
                start=idx
                name=formula[start:end+1]
                val=counter.get(name,0)+num*mul_stack[-1]
                counter[name]=val
                num=1
                idx-=1
        
        ret=[]
        for key in sorted(counter.keys()):
            ret.append(str(key)+(str(counter[key]) if counter[key]>1 else ''))
        return ''.join(ret)

                

# @lc code=end
assert Solution().countOfAtoms("Mg(OH)2")=="H2MgO2"
assert Solution().countOfAtoms('H2O')=='H2O'
assert Solution().countOfAtoms("K4(ON(SO3)2)2")=="K4N2O14S4"
