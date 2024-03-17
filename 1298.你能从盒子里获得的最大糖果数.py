#
# @lc app=leetcode.cn id=1298 lang=python3
#
# [1298] 你能从盒子里获得的最大糖果数
#
from sbw import *
# @lc code=start
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ret=0
        opened_boxs=set()
        closed_boxs=set()
        for b in initialBoxes:
            if status[b]==1:
                opened_boxs.add(b)
            else:
                closed_boxs.add(b)
        while opened_boxs:
            box=opened_boxs.pop()
            ret+=candies[box]
            for k in keys[box]:
                status[k]=1
                if k in closed_boxs:
                    opened_boxs.add(k)
                    closed_boxs.remove(k)
            for b in containedBoxes[box]:
                if status[b]==1:
                    opened_boxs.add(b)
                else:
                    closed_boxs.add(b)
        return ret
# @lc code=end
assert Solution().maxCandies(status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0])==7
assert Solution().maxCandies(status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1])==1
assert Solution().maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0])==6
assert Solution().maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0])==16
