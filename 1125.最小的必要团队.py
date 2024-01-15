#
# @lc app=leetcode.cn id=1125 lang=python3
#
# [1125] 最小的必要团队
#
from sbw import *
# @lc code=start
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        LS=len(req_skills)
        # LP=len(people)
        skills_idx={s:i for i,s in enumerate(req_skills)}
        Mask=1<<LS
        f=[len(people)]*Mask
        f[0]=0
        prev_sk=[0]*Mask
        prev_p=[0]*Mask
        for i,p in enumerate(people):
            if not p:
                continue
            cur=0
            for s in p:
                cur|=1<<(skills_idx[s])
            for prev in range(Mask):
                comb=prev | cur
                if f[comb]>f[prev]+1:
                    f[comb]=f[prev]+1
                    prev_sk[comb]=prev
                    prev_p[comb]=i
        sk=Mask-1
        ret=[]
        while sk>0:
            ret.append(prev_p[sk])
            sk=prev_sk[sk]
        return ret

        
# @lc code=end
assert sorted(Solution().smallestSufficientTeam(req_skills = ["gvp","jgpzzicdvgxlfix","kqcrfwerywbwi","jzukdzrfgvdbrunw","k"], people =   [[],[],[],[],["jgpzzicdvgxlfix"],["jgpzzicdvgxlfix","k"],["jgpzzicdvgxlfix","kqcrfwerywbwi"],["gvp"],["jzukdzrfgvdbrunw"],["gvp","kqcrfwerywbwi"]]
))==sorted([5,8,9])

assert sorted(Solution().smallestSufficientTeam(req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]))==sorted([1,2])
assert Solution().smallestSufficientTeam(req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]])==[0,2]
