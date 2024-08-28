#
# @lc app=leetcode.cn id=699 lang=python3
# @lcpr version=30204
#
# [699] 掉落的方块
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class DynamicNode:
    def __init__(self,left,right) -> None:
        self.l=left
        self.r=right
        self.left:DynamicNode=None
        self.right:DynamicNode=None
        self.val=0
        self.add=0
    
    def pushdown(self):
        mid=(self.l+self.r)>>1
        if not self.left:
            self.left=DynamicNode(self.l,mid)
        if not self.right:
            self.right=DynamicNode(mid+1,self.r)
        if self.add==0:
            return
        self.left.val=self.left.add=self.add
        self.right.val=self.right.add=self.add
        self.add=0
    
    def pushup(self):
        self.val=max(self.left.val,self.right.val)

    def update(self,l,r,val):
        if l<=self.l and r>=self.r:
            self.add=val
            self.val=val
            return
        self.pushdown()
        mid=(self.l+self.r)>>1
        if l<=mid:
            self.left.update(l,r,val)
        if r>mid:
            self.right.update(l,r,val)
        self.pushup()
    
    def query(self,l,r):
        if l<=self.l and r>=self.r:
            return self.val
        self.pushdown()
        mid=(self.l+self.r)>>1
        ret=0
        if l<=mid:
            ret= self.left.query(l,r)
        if r>mid:
            ret=max(ret,self.right.query(l,r))
        return ret

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        Max=max(map(lambda x:sum(x),positions))
        node=DynamicNode(0,Max)
        N=len(positions)
        heights=[0]*N
        for i in range(N):
            left,side=positions[i]
            right=left+side-1
            h=node.query(left,right)
            node.update(left,right,side+h)
            heights[i]=node.val
        return heights
# @lc code=end
assert Solution().fallingSquares([[100,100],[200,100]])==[100,100]
assert Solution().fallingSquares([[1,2],[2,3],[6,1]])==[2,5,5]


#
# @lcpr case=start
# [[1,2],[2,3],[6,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[100,100],[200,100]]\n
# @lcpr case=end

#

