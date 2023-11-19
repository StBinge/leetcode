#
# @lc app=leetcode.cn id=335 lang=python3
#
# [335] 路径交叉
#
from typing import List
# @lc code=start
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        for i in range(3, n):
            # 第 1 类路径交叉的情况
            if (distance[i] >= distance[i - 2]
                    and distance[i - 1] <= distance[i - 3]):
                return True

            # 第 2 类路径交叉的情况
            if i == 4 and (distance[3] == distance[1]
                           and distance[4] >= distance[2] - distance[0]):
                return True

            # 第 3 类路径交叉的情况
            if i >= 5 and (distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3]
                           and distance[i] >= distance[i - 2] - distance[i - 4]
                           and distance[i - 2] > distance[i - 4]):
                return True
        return False


            
                
        

# @lc code=end
assert Solution().isSelfCrossing([2,1,1,2])
assert Solution().isSelfCrossing([1,2,3,4])==False
assert Solution().isSelfCrossing([1,1,2,1,1])==True
assert Solution().isSelfCrossing([1,1,1,1])
