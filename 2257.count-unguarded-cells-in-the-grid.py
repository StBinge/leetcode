#
# @lc app=leetcode.cn id=2257 lang=python3
# @lcpr version=30204
#
# [2257] 统计网格图中没有被保卫的格子数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ret=set()
        rows=defaultdict(list)
        for r,c in guards:
            rows[r].append([c,'g'])
        for r,c in walls:
            rows[r].append([c,'w'])
        
        for rid,row in rows.items():
            row.append([-1,'w'])
            row.append([n,'w'])
            row.sort()
            for i in range(len(row)):
                if row[i][1]=='g':
                    cur=row[i][0]
                    left=row[i-1][0]
                    for j in range(left+1,cur):
                        ret.add((rid,j))
                    right=row[i+1][0]
                    for j in range(cur+1,right):
                        ret.add((rid,j))

        cols=defaultdict(list)
        for r,c in guards:
            cols[c].append([r,'g'])
        for r,c in walls:
            cols[c].append([r,'w'])
        
        for cid,col in cols.items():
            col.append([-1,'w'])
            col.append([m,'w'])
            col.sort()
            for i in range(len(col)):
                if col[i][1]=='g':
                    cur=col[i][0]
                    top=col[i-1][0]
                    for j in range(top+1,cur):
                        ret.add((j,cid))

                    bottom=col[i+1][0]
                    for j in range(cur+1,bottom):
                        ret.add((j,cid))
        return m*n-len(walls)-len(guards)-len(ret)


# @lc code=end
assert Solution().countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]])==4
assert Solution().countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])==7


#
# @lcpr case=start
# 4\n6\n[[0,0],[1,1],[2,3]]\n[[0,1],[2,2],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[[1,1]]\n[[0,1],[1,0],[2,1],[1,2]]\n
# @lcpr case=end

#

