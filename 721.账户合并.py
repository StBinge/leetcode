#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#
from typing import List
# @lc code=start
class Union:
    def __init__(self,n) -> None:
        self.p=list(range(n))
    
    def find(self,x):
        if x!=self.p[x]:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    def connect(self,x,y):
        self.p[self.find(y)]=self.p[self.find(x)]
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail2idx={}
        idx2name={}
        idx=0
        for account in accounts:
            for email in account[1:]:
                if email not in mail2idx:
                    mail2idx[email]=idx
                    idx2name[idx]=account[0]
                    idx+=1
        
        union=Union(len(mail2idx))
        for account in accounts:
            pidx=mail2idx[account[1]]
            for email in account[2:]:
                union.connect(pidx,mail2idx[email])
        
        
        idx2emails={}
        for mail,idx in mail2idx.items():
            pidx=union.find(idx)
            ar=idx2emails.setdefault(pidx,[])
            ar.append(mail)
        
        return [[idx2name[idx],*sorted(malis)] for idx,malis in idx2emails.items()]

# @lc code=end
accounts=[["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
print(Solution().accountsMerge(accounts))


accounts=[["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
print(Solution().accountsMerge(accounts))

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# answer=
print(Solution().accountsMerge(accounts))

accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
print(Solution().accountsMerge(accounts))
