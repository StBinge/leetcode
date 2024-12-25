#
# @lc app=leetcode.cn id=面试题 10.01 lang=python3
# @lcpr version=30204
#
# [面试题 10.01] 合并排序的数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        idx=len(A)-1
        m-=1
        n-=1
        while m>=0 and n>=0:
            if A[m]>=B[n]:
                A[idx]=A[m]
                m-=1
                idx-=1
            else:
                A[idx]=B[n]
                n-=1
                idx-=1
        while m>=0:
            A[idx]=A[m]
            m-=1
            idx-=1
        while n>=0:
            A[idx]=B[n]
            n-=1
            idx-=1
# @lc code=end
A = [1,2,3,0,0,0]
m = 3
B = [2,5,6]
n = 3
Solution().merge(A,m,B,n)
assert A==[1,2,2,3,5,6]

#
# @lcpr case=start
# [1,2,3,0,0,0]\n[2,5,6]\n3\n
# @lcpr case=end

#

