#
# @lc app=leetcode.cn id=1306 lang=python3
#
# [1306] 跳跃游戏 III
#
from sbw import *
# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=[start]
        vis={start}
        L=len(arr)
        while q:
            p=q.pop()
            for i in [1,-1]:
                nxt=p+arr[p]*i
                if 0<=nxt<L:
                    if arr[nxt]==0:
                        return True
                    if nxt not in vis:
                        q.append(nxt)
                        vis.add(nxt)
        return False
# @lc code=end
assert Solution().canReach(arr = [3,0,2,1,2], start = 2)==False
assert Solution().canReach(arr = [4,2,3,0,3,1,2], start = 0)
assert Solution().canReach(arr = [4,2,3,0,3,1,2], start = 5)
