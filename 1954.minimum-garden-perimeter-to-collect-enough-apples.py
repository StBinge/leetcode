#
# @lc app=leetcode.cn id=1954 lang=python3
# @lcpr version=30204
#
# [1954] 收集足够苹果的最小花园周长
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        M=int(math.cbrt(neededApples/4))
        if 2*M*(2*M+1)*(M+1)<neededApples:
            M+=1
        return M*8
            
# @lc code=end
assert Solution().minimumPerimeter(1000000000)==5040
assert Solution().minimumPerimeter(1)==8
assert Solution().minimumPerimeter(13)==16


#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

# @lcpr case=start
# 1000000000\n
# @lcpr case=end

#

