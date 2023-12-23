#
# @lc app=leetcode.cn id=911 lang=python3
#
# [911] 在线选举
#
from tomlkit import key
from sbw import *
# @lc code=start
import bisect
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        Max=0
        counter={}
        rank=[]
        for i in range(len(times)):
            p=persons[i]
            v=counter.get(p,0)+1
            counter[p]=v
            if v<Max:
                continue
            if v>Max:
                Max=v
            if rank and rank[-1][1]==p:
                continue
            rank.append([times[i],p])
        self.rank=rank

    def q(self, t: int) -> int:
        # if t in self.rank:
        #     return self.rank[t]
        l,r=0,len(self.rank)-1
        while l<=r:
            mid=(l+r)>>1
            x=self.rank[mid][0]
            if x<=t:
                l=mid+1
            else:
                r=mid-1
        return self.rank[l-1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

topVotedCandidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
assert topVotedCandidate.q(3)==0
assert topVotedCandidate.q(12)==1
assert topVotedCandidate.q(25)==1
assert topVotedCandidate.q(15)==0
assert topVotedCandidate.q(24)==0
assert topVotedCandidate.q(8)==1