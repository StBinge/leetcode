#
# @lc app=leetcode.cn id=855 lang=python3
#
# [855] 考场就座
#

# @lc code=start
from sortedcontainers import SortedList
class ExamRoom:

    def __init__(self, n: int):
        def dist(x):
            l,r=x
            if l==-1 or r==n:
                return r-l-1
            return (r-l)>>1
        self.n=n
        self.left={n:-1}
        self.right={-1:n}
        self.ts=SortedList(key=lambda x:[-dist(x),x[0]])
        self.ts.add((-1,n))

    def delete(self,seg):
        l,r=seg
        self.ts.remove(seg)
        self.left.pop(r)
        self.right.pop(l)

    def add(self,seg):
        self.ts.add(seg)
        l,r=seg
        self.left[r]=l
        self.right[l]=r

    def seat(self) -> int:
        l,r=self.ts[0]
        self.delete(self.ts[0])
        if l==-1:
            p=0
        elif r==self.n:
            p=self.n-1
        else:
            p=(l+r)>>1
        self.add((l,p))
        self.add((p,r))
        return p


    def leave(self, p: int) -> None:
        l=self.left[p]
        r=self.right[p]
        self.delete((l,p))
        self.delete((p,r))
        self.add((l,r))

# Your ExamRoom object will be instantiated and called as such:
# @lc code=end

obj = ExamRoom(10)
obj.seat()
obj.seat()
obj.seat()
obj.seat()
obj.leave(4)
obj.seat()

