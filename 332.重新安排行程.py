#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
from typing import List
import heapq
# @lc code=start
class Solution:
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        maps:dict[str,list]={}
        for x,y in tickets:
            if x not in maps:
                maps[x]=[]
            maps[x].append(y)
        
        for key in maps:
            heapq.heapify(maps[key])

        ret=[]
        def dfs(cur):
            while cur in maps and maps[cur]:
                temp=heapq.heappop(maps[cur])
                dfs(temp)
            ret.append(cur)

        dfs('JFK')
        return ret[::-1]
# @lc code=end

tickets=[["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
res=Solution().findItinerary(tickets)
print(res)


tickets=[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
res=Solution().findItinerary(tickets)
print(res)

tickets=[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
res=Solution().findItinerary(tickets)
print(res)

tickets=[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
res=Solution().findItinerary(tickets)
print(res)