#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#
from typing import List


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_set = {0}
        queue = [0]
        while queue:
            room = queue.pop()
            keys = rooms[room]
            for k in keys:
                if k in key_set:
                    continue
                key_set.add(k)
                queue.append(k)
        return len(key_set) == len(rooms)


# @lc code=end
rooms = [[1,3],[3,0,1],[2],[0]]
assert Solution().canVisitAllRooms(rooms)==False

rooms = [[1], [2], [3], []]
assert Solution().canVisitAllRooms(rooms)
