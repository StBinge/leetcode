#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#
from sbw import *
# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out=Counter(x for x,y in trust)
        ind=Counter(y for x,y in trust)
        return next((i for i in range(1,n+1) if out[i]==0 and ind[i]==n-1),-1)
# @lc code=end
n=1
trust=[]
assert Solution().findJudge(n,trust)==1
n=4
trust=[[1,3],[1,4],[2,3],[2,4],[4,3]]
assert Solution().findJudge(n,trust)==3

n = 3
trust = [[1,3],[2,3],[3,1]]
assert Solution().findJudge(n,trust)==-1
n = 3
trust = [[1,3],[2,3]]
assert Solution().findJudge(n,trust)==3
