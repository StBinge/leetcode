#
# @lc app=leetcode.cn id=1443 lang=python3
#
# [1443] 收集树上所有苹果的最少时间
#
from sbw import *
# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        edge_map={}
        for p,c in edges:
            edge_map.setdefault(p,[]).append(c)
            edge_map.setdefault(c,[]).append(p)

        def dfs(node:int,prev:int):
            for nxt in edge_map.get(node,[]):
                if nxt==prev:
                    continue
                if dfs(nxt,node):
                    hasApple[node]=True
            return hasApple[node]

        dfs(0,-1)
        
        ret=0
        for s,e in edges:
            if hasApple[s] and hasApple[e]:
                ret+=2
        return ret
# @lc code=end
assert Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = eval_list_str('[false,false,true,false,false,true,false]'))==6
assert Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = eval_list_str('[false,false,false,false,false,false,false]'))==0
assert Solution().minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = eval_list_str('[false,false,true,false,true,true,false]'))==8
