#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#
from sbw import *
# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fi,si=0,0
        fl,sl=len(firstList),len(secondList)
        ret=[]
        while fi<fl and si<sl:
            lo=max(firstList[fi][0],secondList[si][0])
            hi=min(firstList[fi][1],secondList[si][1])
            if lo<=hi:
                ret.append([lo,hi])
            if firstList[fi][1]<=secondList[si][1]:
                fi+=1
            else:
                si+=1
        return ret
# @lc code=end
firstList = [[14,16]]
secondList=[[7,13],[16,20]]
ret=[[16,16]]
assert Solution().intervalIntersection(firstList,secondList)==ret

firstList = [[1,7]]
secondList = [[3,10]]
ret=[[3,7]]
assert Solution().intervalIntersection(firstList,secondList)==ret

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
ret=[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
assert Solution().intervalIntersection(firstList,secondList)==ret
