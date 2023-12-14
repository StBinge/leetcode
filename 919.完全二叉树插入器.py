#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#
from sbw import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        # self.cur_level=[]
        # self.nxt_level=[]
        queue=deque([root])
        self.cnt=0
        while queue:
            self.cnt+=1
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        

    def insert(self, val: int) -> int:
        node=TreeNode(val)
        self.cnt+=1
        p=self.root
        high_bit=self.cnt.bit_length()-2
        for i in range(high_bit,0,-1):
            if self.cnt & 1<<i:
                p=p.right
            else:
                p=p.left
        if self.cnt &1:
            p.right=node
        else:
            p.left=node
        return p.val


    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# @lc code=end
cBTInserter = CBTInserter(TreeNode.build([1, 2,3]))
assert cBTInserter.insert(4)==2
# assert cBTInserter.insert(4)==2 
cBTInserter.get_root().print() 


cBTInserter = CBTInserter(TreeNode.build([1, 2]))
assert cBTInserter.insert(3)==1 
assert cBTInserter.insert(4)==2 
cBTInserter.get_root().print() 
