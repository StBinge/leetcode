#
# @lc app=leetcode.cn id=2397 lang=python3
# @lcpr version=30204
#
# [2397] 被列覆盖的最多行数
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        R, C = len(matrix), len(matrix[0])
        if numSelect == C:
            return R

        row_masks = []
        for row in matrix:
            mask = 0
            for cell in row:
                mask = (mask << 1) + cell
            row_masks.append(mask)

        ret = 0
        mask = 1 << C
        subset = (1 << numSelect) - 1
        while subset < mask:
            covered=sum(row & subset == row for row in row_masks)
            ret = max(ret, covered)
            lb = subset & -subset
            x = subset + lb
            subset = ((subset ^ x) // lb >> 2) | x
        return ret


# @lc code=end
assert Solution().maximumRows([[0, 0, 1], [1, 0, 0], [0, 0, 0]], 2) == 3


def display(name, x):
    print(name, bin(x)[2:].rjust(10, "0"))


subset = 0b1011011
lb = subset & -subset
x = subset + lb
right = (subset ^ x) // lb >> 2
display("subset", subset)
display("lb", lb)
display("x", x)
display("subset^x", subset ^ x)
display("right", right)
#
# @lcpr case=start
# [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1],[0]]\n1\n
# @lcpr case=end

#
