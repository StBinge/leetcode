#
# @lc app=leetcode.cn id=2166 lang=python3
# @lcpr version=30204
#
# [2166] 设计位集
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Bitset:

    def __init__(self, size: int):
        self.flipped=0
        self.bits=[0]*size
        self.cnt1=0
        self.size=size


    def fix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped:
            return
        self.bits[idx]^=1
        self.cnt1+=1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped:
            self.bits[idx]^=1
            self.cnt1-=1

    def flip(self) -> None:
        self.flipped=1- self.flipped
        self.cnt1=self.size-self.cnt1

    def all(self) -> bool:
        return self.cnt1==self.size

    def one(self) -> bool:
        return self.cnt1>0

    def count(self) -> int:
        return self.cnt1

    def toString(self) -> str:
        return ''.join([str(bit ^ self.flipped) for bit in self.bits])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
# @lc code=end

obj=Bitset(5)
ops=["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
args=[[5], [3], [1], [], [], [0], [], [], [0], [], []]
ans='[null, null, null, null, false, null, null, true, null, 2, "01010"]'

test_obj(obj,ops,args,ans)

