#
# @lc app=leetcode.cn id=1462 lang=python3
#
# [1462] 课程表 IV
#
from sbw import *
# @lc code=start
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=[[] for _ in range(numCourses)]
        ret=[]
        is_pre=[[False]*numCourses for _ in range(numCourses)]

        for pre,nxt in prerequisites:
            graph[pre].append(nxt)

        vis=[False]*numCourses
        def dfs(cur):
            if vis[cur]:
                return
            vis[cur]=True
            for nxt in graph[cur]:
                is_pre[cur][nxt]=True
                dfs(nxt)
                for i in range(numCourses):
                    is_pre[cur][i]=is_pre[cur][i] | is_pre[nxt][i]
        for i in range(numCourses):
            dfs(i)
        
        for pre,nxt in queries:
            ret.append(is_pre[pre][nxt])
        return ret

# @lc code=end
assert Solution().checkIfPrerequisite(5,[[0,1],[1,2],[2,3],[3,4]],[[0,4],[4,0],[1,3],[3,0]])==eval_list_str('[true,false,true,false]')
assert Solution().checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])==[True,True]
assert Solution().checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]])==[False,False]
assert Solution().checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])==[False,True]
