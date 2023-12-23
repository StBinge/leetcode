#
# @lc app=leetcode.cn id=913 lang=python3
#
# [913] 猫和老鼠
#

from sbw import *
# @lc code=start
from itertools import product
from collections import defaultdict

DRAW,WIN,LOSE=0,1,2
CAT,MOUSE=1,0
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        # status(first_role,first_role_pos,last_role_pose)
        out={}
        cache=defaultdict(lambda:DRAW)
        q=[]

        def set_result(state,res):
            cache[state]=res
            q.append((state,res))
        

        # for ini,p in product((CAT,MOUSE),range(1,len(graph))):
            # set_result((ini,p,p),WIN if ini==CAT else LOSE)
            # set_result((ini,p,0),LOSE if ini==CAT else WIN) 
        
        for p in range(1,len(graph)):
            set_result((MOUSE,0,p),WIN)
            set_result((MOUSE,p,p),LOSE)
            set_result((MOUSE,p,0),WIN)
            set_result((CAT,p,0),LOSE)
            set_result((CAT,p,p),WIN)

        for sta,result in q:
            for prvip in graph[sta[2]]:
                prvSta=(1^sta[0],prvip,sta[1])
                if prvSta in cache:
                    continue
                if result==LOSE:
                    set_result(prvSta,WIN)
                else:
                    out[prvSta]=out.get(prvSta,len(graph[prvip]))-1
                    if out[prvSta]==0:
                        set_result(prvSta,LOSE)
        return cache[(MOUSE,1,2)]


# @lc code=end
graph=[[5,7,9],[3,4,5,6],[3,4,5,8],[1,2,6,7],[1,2,5,7,9],[0,1,2,4,8],[1,3,7,8],[0,3,4,6,8],[2,5,6,7,9],[0,4,8]]
assert Solution().catMouseGame(graph)==1

graph=[[2,3],[3,4],[0,4],[0,1],[1,2]]
assert Solution().catMouseGame(graph)==1

graph = [[1,3],[0],[3],[0,2]]
assert Solution().catMouseGame(graph)==1

graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
assert Solution().catMouseGame(graph)==0
