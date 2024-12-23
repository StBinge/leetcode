#
# @lc app=leetcode.cn id=2683 lang=python3
# @lcpr version=30204
#
# [2683] 相邻值的按位异或
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(lambda x,y:x^y,derived)==0
# @lc code=end
assert Solution().doesValidArrayExist([1,1,0])
assert Solution().doesValidArrayExist([1,1])
assert Solution().doesValidArrayExist([1,0])==False


#
# @lcpr case=start
# [1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0]\n
# @lcpr case=end

#

