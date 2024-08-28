#
# @lc app=leetcode.cn id=1960 lang=python3
# @lcpr version=30204
#
# [1960] 两个回文子字符串长度的最大乘积
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        f = [1] * N
        R = 0
        L = 0

        for i in range(1, N):
            if i <= R:
                mi = 2 * L - i
                f[i] = min(f[mi], R - i + 1)
            while i - f[i] >= 0 and i + f[i] < N and s[i - f[i]] == s[i + f[i]]:
                f[i] += 1

            if R < i + f[i] - 1:
                R = i + f[i] - 1
                L = i
        start_L=[1]*N
        end_r=[1]*N
        for i,r in enumerate(f):
            left=i-r+1
            right=i+r-1
            l=r*2-1
            start_L[left]=max(start_L[left],l)
            end_r[right]=max(end_r[right],l)

        for i in range(N-2,-1,-1):
            start_L[i]=max(start_L[i],start_L[i+1])
        
        for i in range(1,N):
            start_L[i]=max(start_L[i],start_L[i-1]-2)
        
        for i in range(1,N):
            end_r[i]=max(end_r[i],end_r[i-1])
        for i in range(N-2,-1,-1):
            end_r[i]=max(end_r[i],end_r[i+1]-2)

        return max(end_r[i]*start_L[i+1] for i in range(N-1))
# @lc code=end
assert Solution().maxProduct("ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg") == 45
assert Solution().maxProduct("zaaaxbbby") == 9
assert Solution().maxProduct("zaaaxbbby") == 9
assert Solution().maxProduct("ababbb") == 9


#
# @lcpr case=start
# "ababbb"\n
# @lcpr case=end

# @lcpr case=start
# "zaaaxbbby"\n
# @lcpr case=end

#
