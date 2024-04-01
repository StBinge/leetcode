#
# @lc app=leetcode.cn id=1505 lang=python3
#
# [1505] 最多 K 次交换相邻数位后得到的最小整数
#
from sbw import *
# @lc code=start
class SegTree:
    def __init__(self,n) -> None:
        self.nodes=[0]*(n+1)
        self.n=n
    
    def low_bit(self,x):
        return x&(-x)
    
    def add(self,x):
        while x<=self.n:
            self.nodes[x]+=1
            x+=self.low_bit(x)
    
    def get(self,x):
        ret=0
        while x>0:
            ret+=self.nodes[x]
            x-=self.low_bit(x)
        return ret
    
    def get_range(self,x,y):
        return self.get(y)-self.get(x-1)

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        L=len(num)
        pos=[[] for _ in range(10)]
        for i in range(L-1,-1,-1):
            pos[ord(num[i])-ord('0')].append(i+1)
        
        node=SegTree(L)
        ret=[]
        for i in range(1,L+1):
            for j in range(10):
                if not pos[j]:
                    continue
                p=pos[j][-1]
                behind=node.get_range(p+1,L)
                move=p+behind-i
                if move>k:
                    continue
                k-=move
                pos[j].pop()
                ret.append(str(j))
                node.add(p)
                break
        return ''.join(ret)
# @lc code=end
assert Solution().minInteger('4321',4)=='1342'
