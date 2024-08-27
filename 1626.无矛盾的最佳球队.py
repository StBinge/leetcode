#
# @lc app=leetcode.cn id=1626 lang=python3
#
# [1626] 无矛盾的最佳球队
#
from sbw import *
# @lc code=start
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n=len(scores)
        max_age=max(ages)
        indices=sorted(range(n),key=lambda x: (scores[x],ages[x]))
        tree=[0]*(max_age+1)
        def lowbit(x):
            return x&-x
        def update(age,val):
            while age<=max_age:
                tree[age]=max(tree[age],val)
                age+=lowbit(age)
        def query(age):
            ret=0
            while age:
                ret=max(ret,tree[age])
                age-=lowbit(age)
            return ret
        ret=0
        for i in range(n):
            s,age=scores[indices[i]],ages[indices[i]]
            max_s=s+query(age)
            update(age,max_s)
            ret=max(ret,max_s)
        return ret

# @lc code=end

assert Solution().bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1])==16
assert Solution().bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5])==34