#
# @lc app=leetcode.cn id=1620 lang=python3
#
# [1620] 网络信号最好的坐标
#
from sbw import *


# @lc code=start
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def dist(x1, y1, x2, y2):
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        left=100
        right=0
        top=100
        bottom=0
        for x,y,_ in towers:
            left=min(left,x)
            right=max(right,x)
            top=min(top,y)
            bottom=max(bottom,y)
        max_q = 0
        ret = [0,0]
        for x in range(left,right+1):
            for y in range(top,bottom+1):
        # for x, y, _ in towers:
                tot = 0
                for tx, ty, q in towers:
                    d = dist(x, y, tx, ty)
                    if d > radius:
                        continue
                    tot += int(q / (1 + d))
                tot = tot
                if tot > max_q:
                    max_q = tot
                    ret = [x, y]
        return ret


# @lc code=end
assert Solution().bestCoordinate([[30,34,31],[10,44,24],[14,28,23],[50,38,1],[40,13,6],[16,27,9],[2,22,23],[1,6,41],[34,22,40],[40,10,11]],20) == [1,6]
assert Solution().bestCoordinate([[0,1,2],[2,1,2],[1,0,2],[1,2,2]],1) == [1,1]
assert Solution().bestCoordinate([[42,0,0]],7) == [0,0]
assert Solution().bestCoordinate(towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2) == [1,2]
assert Solution().bestCoordinate(towers=[[23, 11, 21]], radius=9) == [23, 11]
assert Solution().bestCoordinate(
    towers=[[1, 2, 5], [2, 1, 7], [3, 1, 9]], radius=2
) == [2, 1]
