#
# @lc app=leetcode.cn id=1361 lang=python3
#
# [1361] 验证二叉树
#
from sbw import *
# @lc code=start
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents=[-1]*n
        for i in range(n):
            left=leftChild[i]
            if left>=0:
                if parents[left]!=-1:
                    return False
                parents[left]=i
            
            right=rightChild[i]
            if right>=0:
                if parents[right]!=-1:
                    return False
                parents[right]=i
        
        root=-1
        for i in range(n):
            if parents[i]<0:
                if root!=-1:
                    return False
                root=i
        if root==-1:
            return False
        cnt=0
        q=[root]
        while q:
            cur=q.pop()
            cnt+=1
            left,right=leftChild[cur],rightChild[cur]
            if left!=-1:
                q.append(left)
            if right!=-1:
                q.append(right)
        return cnt==n
# @lc code=end
assert Solution().validateBinaryTreeNodes(4,[1,0,3,-1],[-1,-1,-1,-1])==False
assert Solution().validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1])==False
assert Solution().validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1])==False
assert Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])==False
assert Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])
