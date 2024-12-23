#
# @lc app=leetcode.cn id=3249 lang=python3
# @lcpr version=30204
#
# [3249] 统计好节点的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)


        ret=0
        def dfs(cur,pre):
            tot=size=0
            valid=True
            for nxt in adj[cur]:
                if nxt==pre:
                    continue
                cnt=dfs(nxt,cur)
                if size==0:
                    size=cnt
                elif size!=cnt:
                    valid=False
                tot+=cnt
            if valid:
                nonlocal ret
                ret+=1
            return tot+1

        dfs(0,-1)
        return ret

# @lc code=end
assert Solution().countGoodNodes( [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]])==6
assert Solution().countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])==7


#
# @lcpr case=start
# [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]\n
# @lcpr case=end

#

