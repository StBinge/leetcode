#
# @lc app=leetcode.cn id=1261 lang=python3
#
# [1261] 在受污染的二叉树中查找元素
#
from sbw import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # root.val=0
        # self.memo={}
        # q=[[1,root]]
        # while q:
        #     val,node=q.pop()
        #     node.val=val
        #     if node.left:
        #         q.append([val*2,node.left])
        #     if node.right:
        #         q.append([val*2+1,node.right])
        self.root=root

    def find(self, target: int) -> bool:
        target+=1
        hibit=1
        d=0
        while hibit<=target:
            d+=1
            hibit<<=1
        d-=1
        root=self.root
        for i in range(d-1,-1,-1):
            if target & (1<<i):
                root=root.right
            else:
                root=root.left
            if not root:
                return False
        return True



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end
obj=FindElements(TreeNode.build('[-1,-1,-1,-1,-1]'))
assert obj.find(1)
assert obj.find(3)
assert obj.find(5)==False

obj=FindElements(TreeNode.build('[-1,null,-1]'))
assert obj.find(1)==False
assert obj.find(2)
