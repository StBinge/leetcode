#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import Optional
# @lc code=start
# Definition for a binary tree node.

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        vals=[]
        def postorder(node:TreeNode):
            if not node:
                return 
            postorder(node.left)
            postorder(node.right)
            vals.append(node.val)
        postorder(root)
        return ' '.join(map(str,vals))


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        vals=list(map(int,data.split()))

        def construct(lower,upper):
            if not vals or vals[-1]>upper or vals[-1]<lower:
                return None
            val=vals.pop()
            node=TreeNode(val)
            node.right=construct(val,upper)
            node.left=construct(lower,val)
            return node
        return construct(-1,10**5)
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

