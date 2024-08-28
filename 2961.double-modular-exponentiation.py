#
# @lc app=leetcode.cn id=2961 lang=python3
# @lcpr version=30204
#
# [2961] 双模幂运算
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ret = []
        for i in range(len(variables)):
            a, b, c, m = variables[i]
            if (pow(a, b, 10) ** c) % m == target:
                ret.append(i)
        return ret


# @lc code=end
assert Solution().getGoodIndices(variables=[[39, 3, 1000, 1000]], target=17) == []
assert Solution().getGoodIndices(
    variables=[[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], target=2
) == [0, 2]


#
# @lcpr case=start
# [[2,3,3,10],[3,3,3,1],[6,1,1,4]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[39,3,1000,1000]]\n17\n
# @lcpr case=end

#
