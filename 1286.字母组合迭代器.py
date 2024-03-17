#
# @lc app=leetcode.cn id=1286 lang=python3
#
# [1286] 字母组合迭代器
#

# @lc code=start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        L=len(characters)
        self.indices=list(range
        (combinationLength))
        self.max_indices=[L-i for i in range(combinationLength,0,-1)]
        self.chars=characters
        self.n=combinationLength
        self.end=False

    def change_indices(self):
        # L=len(self.chars)
        j=-1
        for i in range(self.n-1,-1,-1):
            if self.indices[i]<self.max_indices[i]:
                j=i
                break
        if j<0:
            self.end=True
            return
        self.indices[j]+=1
        for i in range(j+1,self.n):
            self.indices[i]=self.indices[i-1]+1
    def next(self) -> str:
        ret=[]
        for i in range(self.n):
            ret.append(self.chars[self.indices[i]])
        # self.indices[-1]+=1
        self.change_indices()
        return ''.join(ret)

    def hasNext(self) -> bool:
        return not self.end


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
from itertools import combinations
ops=["hasNext","next","hasNext","next","hasNext","next","next","next","hasNext","hasNext","next","hasNext","hasNext","next","hasNext","next","hasNext","hasNext","hasNext","next","next","hasNext","next","hasNext","next","next","hasNext","hasNext","next","next","hasNext","hasNext","next","hasNext","next","next","next","next","hasNext","hasNext","next","next","hasNext","hasNext","next","next","hasNext","next","hasNext","hasNext","hasNext","next","next","hasNext","hasNext","hasNext","hasNext","next","hasNext","next","hasNext","next","next","next","next","next","next","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext"]

itor=CombinationIterator('fiklnuy',3)
comb=combinations('fiklnuy',3)
for op in ops:
    if op=='hasNext':
        itor.hasNext()
    else:
        r1= itor.next()
        # r2=''.join(next(comb))
        # assert r1==r2
        print(r1)


itor=CombinationIterator('abc',2)
assert itor.next()=='ab'
assert itor.hasNext()
assert itor.next()=='ac'
assert itor.hasNext()
assert itor.next()=='bc'
assert itor.hasNext()==False
