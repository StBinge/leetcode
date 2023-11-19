#
# @lc app=leetcode.cn id=699 lang=python3
#
# [699] 掉落的方块
#
from typing import List
# @lc code=start
class SegmentTree:
    def __init__(self,left,right,val=0) -> None:
        self.l=left
        self.r=right
        self.val=val
        self.left=None
        self.right=None
        self.lazy=0
        # self.update=val
    
    def modify(self,l,r,val):
        if l>r:
            return
        if l<=self.l and r>=self.r:
            self.val=val
            self.lazy=val
            return
        self.pushdown()
        mid=(self.l+self.r)//2
        if l<=mid:
            self.left.modify(l,r,val)
        if r>mid:
            self.right.modify(l,r,val)
        self.val=max(self.left.val,self.right.val)
    
    def pushdown(self):
        mid=(self.l+self.r)//2
        if not self.left:
            self.left=SegmentTree(self.l,mid)
        if not self.right:
            self.right=SegmentTree(mid+1,self.r)
        if self.lazy:
            self.left.val=self.left.lazy=self.right.val=self.right.lazy=self.lazy
            self.lazy=0


    def query(self,l,r):
        if l>r:
            return 0
        if l<=self.l and r>=self.r:
            return self.val
        self.pushdown()
        mid=(self.l+self.r)//2
        v=0
        if l<=mid:
            v=max(v,self.left.query(l,r))
        if r>mid:
            v=max(self.right.query(l,r),v)
        return v

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        tree=SegmentTree(1,10**8,0)
        # tree.modify()
        ret=[]
        # mx=0
        for left,width in positions:
            right=left+width-1
            h=tree.query(left,right)+width

            tree.modify(left,right,h)
            # mx=max(h,mx)
            # ret.append(max(h,ret[-1] if ret else 0))
            ret.append(tree.val)
        return ret

# @lc code=end
positions=[[4,9],[8,8],[6,8],[8,2],[1,2]]
assert Solution().fallingSquares(positions)==[9,17,25,27,27]

positions = [[9,1],[6,5],[6,7]]
assert Solution().fallingSquares(positions)==[1,6,13]

positions = [[1,2],[1,3]]
assert Solution().fallingSquares(positions)==[2,5]

positions = [[1,2],[2,3],[6,1]]
assert Solution().fallingSquares(positions)==[2,5,5]

positions = [[100,100],[200,100]]
assert Solution().fallingSquares(positions)==[100,100]
