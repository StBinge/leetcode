#
# @lc app=leetcode.cn id=2657 lang=python3
# @lcpr version=30204
#
# [2657] 找到两个数组的前缀公共数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N=len(A)
        s=set()
        ret=[0]*N

        for i in range(N-1,-1,-1):
            ret[i]=N-len(s)
            s.add(A[i])
            s.add(B[i])
        return ret

# @lc code=end
assert Solution().findThePrefixCommonArray([1,3,2,4],[3,1,2,4])==[0,2,3,4]


#
# @lcpr case=start
# [1,3,2,4]\n[3,1,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,1]\n[3,1,2]\n
# @lcpr case=end

#

