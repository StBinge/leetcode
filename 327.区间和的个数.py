#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
from typing import List
# @lc code=start
# class SegNode:
#     def __init__(self,left,right) -> None:
#         self.left=left
#         self.right=right
#         self.left_node=None
#         self.right_node=None
#         self.sum=0
    
#     @classmethod
#     def build(cls,left,right):
#         node=SegNode(left,right)
#         if left==right:
#             return node
#         mid=(left+right)//2
#         l_node=SegNode.build(left,mid)
#         r_node=SegNode.build(mid+1,right)
#         node.left_node=l_node
#         node.right_node=r_node
#         return node
    
#     def count(self,left,right):
#         if self.right< left or self.left>right:
#             return 0
#         if self.left>=left and self.right<=right:
#             return self.sum
#         return self.left_node.count(left,right)+self.right_node.count(left,right)

#     def insert(self,index):
#         self.sum+=1
#         if self.left==self.right:
#             return
#         mid=(self.left+self.right)//2
#         if index<=mid:
#             self.left_node.insert(index)
#         else:
#             self.right_node.insert(index)


class Tree:
    def __init__(self,count) -> None:
        self.tree=[0]*(count+1)
        self.len=count+1
    
    def _lowbit(self,index):
        return index&-index

    def add(self,index):
        while index<self.len:
            self.tree[index]+=1
            index+=self._lowbit(index)
    
    def query(self,index):
        ret=0
        while index>0:
            ret+=self.tree[index]
            index-=self._lowbit(index)
        return ret

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # ret=0
        N=len(nums)
        presum=[0]*(N+1)
        # l_bound,r_bound=float('inf'),float('-inf')
        for i in range(N):
            sum=nums[i]+presum[i]
            presum[i+1]=sum
            # l=sum-upper
            # r=sum-lower
            # l_bound=min(l_bound,sum,l,r)
            # r_bound=max(r_bound,sum,l,r)
        
        all_nums=set()
        for sum in presum:
            all_nums.add(sum)
            all_nums.add(sum-lower)
            all_nums.add(sum-upper)

        all_nums=sorted(all_nums)
        num_idx={}
        idx=0
        for n in all_nums:
            num_idx[n]=idx
            idx+=1
        
        Len=len(num_idx.values())
        # node=SegNode.build(l_bound,r_bound)
        tree=Tree(Len)

        ret=0
        for n in presum:
            ret+=tree.query(num_idx[n-lower]+1)-tree.query(num_idx[n-upper])
            tree.add(num_idx[n]+1)
        return ret


        


        
# @lc code=end
nums = [2147483647,-2147483648,-1,0]
lower = -1
upper = 0
assert Solution().countRangeSum(nums,lower,upper)==4


nums = [0]
lower = 0
upper = 0
assert Solution().countRangeSum(nums,lower,upper)==1
nums = [-2,5,-1]
lower = -2
upper = 2
assert Solution().countRangeSum(nums,lower,upper)==3

