#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#
from sbw import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class KMP:
    def __init__(self,pattern:list) -> None:
        L=len(pattern)
        self.pattern=pattern
        self.next=[0]*(L)
        k=0
        for i in range(1,L):
            while pattern[i]!=pattern[k] and k>0:
                k=self.next[k]
            if pattern[i]==pattern[k]:
                k+=1
                self.next[i]=k

    def math(self,target:list):
        k=0
        for i in range(len(target)):
            while target[i]!=self.pattern[k] and k>0:
                k=self.next[k-1]
            if target[i]==self.pattern[k]:
                k+=1
                if k==len(self.pattern):
                    return True

        return False


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        lnull=-10**5
        rnull=10**5
        def traverse(node:TreeNode,seq:list):
            nonlocal lnull,rnull
            if not node:
                return
            seq.append(node.val)
            if node.left:
                traverse(node.left,seq)
            else:
                seq.append(lnull)
            if node.right:
                traverse(node.right,seq)
            else:
                seq.append(rnull)
        pattern=[]
        traverse(subRoot,pattern)
        target=[]
        traverse(root,target)
        return KMP(pattern).math(target)
        
# @lc code=end
kmp=KMP('123123')

print(kmp.next)
print(kmp.math('123121123'))
assert Solution().isSubtree(TreeNode.build('[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]'),TreeNode.build('[1,null,1,null,1,null,1,null,1,null,1,2]'))
assert Solution().isSubtree(TreeNode.build('[3,4,5,1,null,2]'),TreeNode.build([3,1,2]))==False
assert Solution().isSubtree(TreeNode.build([1,1]),TreeNode.build([1]))
