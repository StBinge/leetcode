#
# @lc app=leetcode.cn id=2022 lang=python3
# @lcpr version=30204
#
# [2022] 将一维数组转变成二维数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        N=len(original)
        if m*n!=N:
            return []
        ret=[]
        for i in range(m):
            ret.append(original[i*n:i*n+n])
        return ret
# @lc code=end
assert Solution().construct2DArray(original = [1,2,3,4], m = 2, n = 2)==[[1,2],[3,4]]


#
# @lcpr case=start
# [1,2,3,4]\n2\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n1\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# [3]\n1\n2\n
# @lcpr case=end

#

