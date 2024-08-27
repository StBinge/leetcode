#
# @lc app=leetcode.cn id=2101 lang=python3
# @lcpr version=30204
#
# [2101] 引爆最多的炸弹
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)

        f=[0]*N

        for i in range(N):
            f[i]|=1<<i
            x1, y1, r1 = bombs[i]
            for k in range(i + 1, N):
                x2, y2, r2 = bombs[k]
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist <= r1**2:
                    f[i]|=1<<k
                if dist<=r2**2:
                    f[k]|=1<<i
        
        for i in range(N):
            for k in range(N):
                if f[i]>>k &1:
                    f[i]|=f[k]
        return max(s.bit_count() for s in f)



# @lc code=end
assert Solution().maximumDetonation([[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]) == 9
assert Solution().maximumDetonation([[2, 1, 3], [6, 1, 4]]) == 2
assert (
    Solution().maximumDetonation(
        [
            [54, 95, 4],
            [99, 46, 3],
            [29, 21, 3],
            [96, 72, 8],
            [49, 43, 3],
            [11, 20, 3],
            [2, 57, 1],
            [69, 51, 7],
            [97, 1, 10],
            [85, 45, 2],
            [38, 47, 1],
            [83, 75, 3],
            [65, 59, 3],
            [33, 4, 1],
            [32, 10, 2],
            [20, 97, 8],
            [35, 37, 3],
        ]
    )
    == 1
)
assert Solution().maximumDetonation([[1, 1, 5], [10, 10, 5]]) == 1
assert (
    Solution().maximumDetonation(
        [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    )
    == 5
)


#
# @lcpr case=start
# [[2,1,3],[6,1,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,5],[10,10,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]\n
# @lcpr case=end

#
