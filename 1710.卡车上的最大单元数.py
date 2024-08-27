#
# @lc app=leetcode.cn id=1710 lang=python3
#
# [1710] 卡车上的最大单元数
#
from sbw import *
# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        ret=0
        for x,y in boxTypes:
            added=min(x,truckSize)
            truckSize-=added
            ret+=added*y
            if truckSize==0:
                break
        return ret

# @lc code=end
assert Solution().maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4)==8
