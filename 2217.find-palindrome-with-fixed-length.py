#
# @lc app=leetcode.cn id=2217 lang=python3
# @lcpr version=30204
#
# [2217] 找到指定长度的回文数
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength + 1) // 2
        ret = []
        Base = 10 ** (half - 1)
        Max = 9 * Base
        for q in queries:
            if q > Max:
                ret.append(-1)
                continue

            x=Base+q-1
            xx=x
            if intLength&1:
                xx//=10
            while xx:
                x=x*10+xx%10
                xx//=10
            ret.append(x)
        return ret


# @lc code=end
assert Solution().kthPalindrome([1,2,3,4,5,6,7,8,9,10,11,12,13,14,9,8],1) == [1,2,3,4,5,6,7,8,9,-1,-1,-1,-1,-1,9,8]
assert Solution().kthPalindrome(queries = [2,4,6], intLength = 4) == [1111,1331,1551]
assert Solution().kthPalindrome(queries=[1, 2, 3, 4, 5, 90], intLength=3) == [
    101,
    111,
    121,
    131,
    141,
    999,
]


#
# @lcpr case=start
# [1,2,3,4,5,90]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6]\n4\n
# @lcpr case=end

#
