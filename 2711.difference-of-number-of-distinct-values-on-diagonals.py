#
# @lc app=leetcode.cn id=2711 lang=python3
# @lcpr version=30204
#
# [2711] 对角线上不同值的数量差
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        ret = [[0] * C for _ in range(R)]

        def walk(rr,cc):
            rb = defaultdict(int)
            r=rr
            c = cc
            while 0 <= r < R and 0 <= c < C:
                rb[grid[r][c]] += 1
                r += 1
                c += 1
            lt = defaultdict(int)
            r = rr
            c = cc
            while 0 <= r < R and 0 <= c < C:
                if rb[grid[r][c]] == 1:
                    del rb[grid[r][c]]
                else:
                    rb[grid[r][c]] -= 1
                ret[r][c] = abs(len(lt) - len(rb))
                lt[grid[r][c]] += 1
                r += 1
                c += 1

        for r in range(R):
            walk(r,0)
        for c in range(1,C):
            walk(0,c)
        return ret


# @lc code=end
assert Solution().differenceOfDistinctValues([[1,2,3],[3,1,5],[3,2,1]])==[[1,1,0],[1,0,1],[0,1,1]]

#
# @lcpr case=start
# [[1,2,3],[3,1,5],[3,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#
