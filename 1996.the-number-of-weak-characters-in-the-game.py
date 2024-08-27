#
# @lc app=leetcode.cn id=1996 lang=python3
# @lcpr version=30204
#
# [1996] 游戏中弱角色的数量
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start



class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
  
        ret = 0
        properties.sort(key=lambda x:[-x[0],x[1]])
        mxd=0
        for a,d in properties:
            if d<mxd:
                ret+=1
            else:
                mxd=d
        return ret

# @lc code=end
assert (
    Solution().numberOfWeakCharacters(
        [
            [7, 7],
            [1, 2],
            [9, 7],
            [7, 3],
            [3, 10],
            [9, 8],
            [8, 10],
            [4, 3],
            [1, 5],
            [1, 5],
        ]
    )
    == 6
)
assert Solution().numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]) == 1
assert Solution().numberOfWeakCharacters([[2, 2], [3, 3]]) == 1
assert Solution().numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]) == 0


#
# @lcpr case=start
# [[5,5],[6,3],[3,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5],[10,4],[4,3]]\n
# @lcpr case=end

#
