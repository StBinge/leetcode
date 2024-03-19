#
# @lc app=leetcode.cn id=1376 lang=python3
#
# [1376] 通知所有员工所需的时间
#
from sbw import *
# @lc code=start
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        for i,ma in enumerate(manager):
            if ma<0:
                continue
            x=i
            s=0
            while manager[x]>=0:
                s+=informTime[x]
                x=manager[x]
            
            s+=informTime[x]
            x=i
            while manager[x]>=0:
                informTime[x],s=s,s-informTime[x]
                manager[x],x=-1,manager[x]
        return max(informTime)
# @lc code=end
assert Solution().numOfMinutes(7,6,[1,2,3,4,5,6,-1],[0,6,5,4,3,2,1])==21
assert Solution().numOfMinutes(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])==3
assert Solution().numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0])==1
assert Solution().numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0])==0
