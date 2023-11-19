#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
import math
class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        d=int(math.sqrt(c))
        left,right=0,d
        while left<=right:
            s= left*left+right*right
            if s>c:
                right-=1
            elif s<c:
                left+=1
            else:
                return True
        return False

        
# @lc code=end

assert Solution().judgeSquareSum(0)
assert Solution().judgeSquareSum(1)
assert Solution().judgeSquareSum(2)
assert Solution().judgeSquareSum(4)
assert Solution().judgeSquareSum(5)
assert Solution().judgeSquareSum(3)==False