#
# @lc app=leetcode.cn id=1366 lang=python3
#
# [1366] 通过投票对团队排名
#
from sbw import *
# @lc code=start
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes)==1:
            return votes[0]
        L=len(votes[0])
        if L==1:
            return votes[0]
        ranks={}
        for vote in votes:
            for i in range(L):
                ch=vote[i]
                ranks.setdefault(ch,[0]*L)[i]+=1
        result=sorted(ranks.items(),key=lambda x:[x[1],-(ord(x[0])-ord('A'))],reverse=True)
        return ''.join(ch for ch,_ in result)
# @lc code=end
assert Solution().rankTeams(["M","M","M","M"])=='M'
assert Solution().rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"])=='ABC'
assert Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"])=='ZMNAGUEDSJYLBOPHRQICWFXTVK'
assert Solution().rankTeams(["WXYZ","XYZW"])=='XWYZ'
assert Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"])=='ACB'
