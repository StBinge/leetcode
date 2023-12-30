#
# @lc app=leetcode.cn id=996 lang=python3
#
# [996] 正方形数组的数目
#
from sbw import *
# @lc code=start
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        counter=Counter(nums)
        keys=sorted(counter.keys())
        edges={}
        L=len(keys)
        for i in range(L):
            for j in range(i,L):
                s=keys[i]+keys[j]
                if int(s**0.5 + 0.5)**2==s:
                    edges.setdefault(keys[i],set()).add(keys[j])
                    edges.setdefault(keys[j],set()).add(keys[i])
        
        def pick(cur,left):
            if left==0:
                return 1
            if cur not in edges:
                return 0
            counter[cur]-=1
            ans=0
            for nxt in edges[cur]:
                if counter[nxt]>0:
                    ans+=pick(nxt,left-1)
            counter[cur]+=1
            return ans
        return sum(pick(k,len(nums)-1) for k in keys)
# @lc code=end
assert Solution().numSquarefulPerms([1,1])==0
assert Solution().numSquarefulPerms([0,0,0,1,1,1])==4
assert Solution().numSquarefulPerms([2,2,2])==1
assert Solution().numSquarefulPerms([1,17,8])==2
