#
# @lc app=leetcode.cn id=1707 lang=python3
#
# [1707] 与数组中元素的最大异或值
#
from sbw import *
# @lc code=start
class Tree:
    def __init__(self) -> None:
        self.left:Tree=None
        self.right:Tree=None
        self.has_value=False
        self.val=0
    
    def insert(self,x):
        cur=self
        for i in range(30,-1,-1):
            if x&(1<<i):
                if not cur.right:
                    cur.right=Tree()
                cur=cur.right
            else:
                if not cur.left:
                    cur.left=Tree()
                cur=cur.left
        cur.val=x
    
    def get_max_or(self,val):
        node=self
        for i in range(30,-1,-1):
            bit=(val>>i) & 1
            if bit:
                node=node.left or node.right
            else:
                node=node.right or node.left
            if not node:
                return -1
        return  val ^ node.val
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        root=Tree()
        nums=sorted(set(nums))
        L=len(queries)
        q_idx=sorted(range(L),key=lambda x:queries[x][1])
        ret=[-1]*L
        idx=0
        N=len(nums)
        for q in q_idx:
            x,m=queries[q]
            while idx<N and nums[idx]<=m:
                root.insert(nums[idx])
                idx+=1
            ret[q]=root.get_max_or(x)
        return ret
            
# @lc code=end
assert Solution().maximizeXor([0,3090096,4194304,845573555,0,778971744,267447,0,4194304,4194304,446819176,45001354,4194304,3777171,873518539,0,1165390,4194304,3372544,0],[[4194304,1000000000],[280475304,1000000000],[536870912,1000000000],[1000000000,1000000000],[668787504,391894850],[536870912,3143980],[1000000000,619304916],[453771895,1000000000],[1000000000,1000000000],[4194304,1000000000],[536870912,66331],[308138274,1000000000],[536870912,240619799],[4194304,1000000000],[536870912,4194304],[315860359,1000000000],[4194304,4194304],[1000000000,1000000000],[4194304,1000000000],[1000000000,994164423]])==[877712843,1054448840,983690088,1004194304,670287232,539961008,1004194304,895625239,1004194304,877712843,536870912,1010039618,581872266,877712843,541065216,1019056103,7971475,1004194304,877712843,1004194304]
assert Solution().maximizeXor([2789,2334,389287485,33554432,937557817],[[815049,259443277],[33554432,1000000000],[270557,104302223],[864045667,1000000000],[21219239,1000000000]])==[34369481,904003385,33824989,864043901,916600990]
assert Solution().maximizeXor([818702963,153655392,4096,917434814,4096],[[11886620,881210474],[811373,1000000000],[20352316,1000000000],[443746890,860009574],[872954994,1000000000]])==[813238895,916623571,932740226,717185081,1025549330]
assert Solution().maximizeXor([5,8,0,3,2,10,9,2,4,5],[[3,8]])==[11]
assert Solution().maximizeXor([536870912,0,534710168,330218644,142254206],[[558240772,1000000000],[307628050,1000000000],[3319300,1000000000],[2751604,683297522],[214004,404207941]])==[1050219420,844498962,540190212,539622516,330170208]
assert Solution().maximizeXor(nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]])==[3,3,7]
