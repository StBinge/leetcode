#
# @lc app=leetcode.cn id=1452 lang=python3
#
# [1452] 收藏清单
#
from sbw import *
# @lc code=start
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        L=len(favoriteCompanies)
        fav_sets=list(map(set,favoriteCompanies))
        tops=set(range(L))
        for i in range(L):
            if i not in tops:
                continue
            for j in range(i+1,L):
                if j not in tops:
                    continue
                if fav_sets[i].issubset(fav_sets[j]):
                    tops.discard(i)
                if fav_sets[j].issubset(fav_sets[i]):
                    tops.discard(j)
                if i not in tops:
                    break
        return sorted(tops)
# @lc code=end

assert Solution().peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]])==[0,1,2,3] 
assert Solution().peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]])==[0,1] 
assert Solution().peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]])==[0,1,4] 