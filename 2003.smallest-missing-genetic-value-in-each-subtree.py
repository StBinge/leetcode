#
# @lc app=leetcode.cn id=2003 lang=python3
# @lcpr version=30204
#
# [2003] 每棵子树内缺失的最小基因值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Seg:
    def __init__(self) -> None:
        self.n=10**5+2
        self.vals=[10**9]*(self.n)
        self.small=1
    
    def add(self,tick,val):
        # while x<=self.n:
        #     self.vals[x]+=1
        #     x+=x&-x
        self.vals[val]=tick
        while self.vals[self.small]<=tick:
            self.small+=1
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        N=len(nums)
        deg =[0]*N
        for i,p in enumerate(parents):
            deg[p]+=1
        
        q=[i for i,d in enumerate(deg) if d==0]
        gens=[set(0) for _ in range(N)] 
        while q:
            cur=q.pop()
            


            
        
# @lc code=end
assert Solution().smallestMissingValueSubtree(parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3])==[7,1,1,4,2,1]
assert Solution().smallestMissingValueSubtree(parents = [-1,0,0,2], nums = [1,2,3,4])==[5,1,1,1]


#
# @lcpr case=start
# [-1,0,0,2]\n[1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,1,0,3,3]\n[5,4,6,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,2,3,0,2,4,1]\n[2,3,4,5,6,7,8]\n
# @lcpr case=end

#

