#
# @lc app=leetcode.cn id=1111 lang=python3
#
# [1111] 有效括号的嵌套深度
#
from sbw import *
# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ret=[0]*len(seq)
        for i,c in enumerate(seq):
            ret[i]=(1&i) ^ (c=='(')
        return ret
# @lc code=end
def validate(seq:str):
    stack=[]
    for c in seq:
        if c=='(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack)==0

def depth(seq:str):
    d=0
    ret=0
    for c in seq:
        if c=='(':
            d+=1
        else:
            d-=1
        ret=max(ret,d)
    return ret

seq="()(())()"
ret= Solution().maxDepthAfterSplit(seq)
seqs=[[],[]]
for idx,c in zip(ret,seq):
    seqs[idx].append(c)

assert all(validate(seq) for seq in seqs)
assert max(depth(s) for s in seqs)==1

seq="(()())"
ret= Solution().maxDepthAfterSplit(seq)
seqs=[[],[]]
for idx,c in zip(ret,seq):
    seqs[idx].append(c)

assert all(validate(seq) for seq in seqs)
assert max(depth(s) for s in seqs)==1
