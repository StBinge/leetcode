#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row=[poured]
        
        for r in range(1,query_row+1):
            nxt_row=[0]*(r+1)
            # nxt_row.append()
            for i in range(r):
                if row[i]<=1:
                    continue
                over=row[i]-1
                nxt_row[i]+=over/2
                nxt_row[i+1]+=over/2
            row=nxt_row
        return min(1,row[query_glass])
# @lc code=end
poured = 100000009
query_row = 33
query_glass = 17
assert Solution().champagneTower(poured,query_row,query_glass)==1

poured = 1
query_row = 1
query_glass = 1
assert Solution().champagneTower(poured,query_row,query_glass)==0

poured = 2
query_row = 1
query_glass = 1
assert Solution().champagneTower(poured,query_row,query_glass)==0.5