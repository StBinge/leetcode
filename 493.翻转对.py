#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
from typing import List
# @lc code=start
class Tree:
    def __init__(self,length) -> None:
        self.slots=[0]*(length+1)
        self.n=length

    def lowbit(self,x):
        return x&(-x)

    def add(self,idx,val):
        while idx<=self.n:
            self.slots[idx]+=val
            idx+=self.lowbit(idx)
    
    def query(self,idx):
        cnt=0
        while idx:
            cnt+=self.slots[idx]
            idx-=self.lowbit(idx)
        return cnt

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        all_nums=set(nums)
        all_nums.update([n*2 for n in nums])
        idx=1
        maps={}
        for n in sorted(all_nums):
            if n not in maps:
                maps[n]=idx
                idx+=1
        
        N=len(maps)
        tree=Tree(N)
        ret=0
        for n in nums:
            all_cnt=tree.query(N)
            target=tree.query(maps.get(2*n))
            ret+=all_cnt-target
            tree.add(maps.get(n),1)
        return ret

# @lc code=end

assert Solution().reversePairs([-5,-5])==1
assert Solution().reversePairs([1,3,2,3,1])==2
assert Solution().reversePairs([2,4,3,5,1])==3