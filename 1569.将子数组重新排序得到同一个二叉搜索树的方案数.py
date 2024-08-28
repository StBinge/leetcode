#
# @lc app=leetcode.cn id=1569 lang=python3
#
# [1569] 将子数组重新排序得到同一个二叉搜索树的方案数
#
from sbw import *
# @lc code=start
class Node:
    def __init__(self) -> None:
        self.left=None
        self.right=None
        # self.val=val
        self.size=1
        self.ans=0
    
    def insert(self,val):
        self.childs+=1
        if val<self.val:
            if not self.left:
                self.left=Node(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right=Node(val)
            else:
                self.right.insert(val)
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        Mod=10**9+7
        N=len(nums)
        if N<3:
            return 0
        comb=[[0]*N for _ in range(N)]
        comb[0][0]=1
        for i in range(1,N):
            comb[i][0]=1
            for j in range(1,i+1):
                comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%Mod
        
        parents=list(range(N))
        roots=list(range(N))
        size=[1]*N

        def find(x):
            if parents[x]==x:
                return x
            parents[x]=find(parents[x])
            return parents[x]
        def root(x):
            return roots[find(x)]
        def union(x,y):
            px,py=find(x),find(y)
            roots[py]=roots[px]
            if size[py]>size[px]:
                px,py=py,px
            parents[py]=px
            size[px]+=size[py]

        nodes={}
        for val in reversed(nums):
            val-=1
            node=Node()
            if val-1 in nodes:
                l_child=root(val-1)
                node.left=nodes[l_child]
                node.size+=node.left.size
                union(val,l_child)
            if val+1 in nodes:
                r_child=root(val+1)
                node.right=nodes[r_child]
                node.size+=node.right.size
                union(val,r_child)
            l_size=node.left.size if node.left else 0
            r_size=node.right.size if node.right else 0
            l_ans=node.left.ans if node.left else 1
            r_ans=node.right.ans if node.right else 1
            node.ans=(comb[l_size+r_size][l_size]*l_ans*r_ans)%Mod
            nodes[val]=node
        return (nodes[nums[0]-1].ans-1)%Mod

# @lc code=end
assert Solution().numOfWays([3,4,5,1,2])==5
assert Solution().numOfWays([2,1,3])==1
