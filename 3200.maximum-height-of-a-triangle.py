#
# @lc app=leetcode.cn id=3200 lang=python3
# @lcpr version=30204
#
# [3200] 三角形的最大高度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import math
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # K odd rows
        # 1+3+...+2*K-1=>(1+2*K-1)*K//2=K^2

        # K even rows
        # 2+4+6...+2*K=>(2+2*K)*K//2=K+K^2
        def check(x,y):
            odd=math.isqrt(x)
            even=int(math.sqrt(y+1/4)-0.5)
            if odd>even:
                return 2*even+1
            else:
                return 2*odd
        
        return max(check(red,blue),check(blue,red))
# @lc code=end
assert Solution().maxHeightOfTriangle(2,4)==3
assert Solution().maxHeightOfTriangle(2,3)==2
assert Solution().maxHeightOfTriangle(10,1)==2
assert Solution().maxHeightOfTriangle(1,1)==1
assert Solution().maxHeightOfTriangle(2,1)==2


#
# @lcpr case=start
# 2\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n1\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

# @lcpr case=start
# 10\n1\n
# @lcpr case=end

#

