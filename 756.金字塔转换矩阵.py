#
# @lc app=leetcode.cn id=756 lang=python3
#
# [756] 金字塔转换矩阵
#
from typing import List
# @lc code=start
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        T = [[0] * (1 << 7) for _ in range(1 << 7)]
        for triple in allowed:
            u, v, w = (1 << (ord(x) - ord('A')) for x in triple)
            for b1 in range(1 << 7):
                if u & b1:
                    for b2 in range(1 << 7):
                        if v & b2:
                            T[b1][b2] |= w

        state = [1 << (ord(x) - ord('A')) for x in bottom]
        while len(state) > 1:
            for i in range(len(state) - 1):
                state[i] = T[state[i]][state[i+1]]
            state.pop()
        return bool(state[0])


# @lc code=end
bottom="DBCDA"
allowed=["DBD","BCC","CDD","DAD","DDA","AAC","CCA","BCD"]
assert Solution().pyramidTransition(bottom,allowed)

bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]
assert Solution().pyramidTransition(bottom,allowed)
bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]
assert Solution().pyramidTransition(bottom,allowed)==False
