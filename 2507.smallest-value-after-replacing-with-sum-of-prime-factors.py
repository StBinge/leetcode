#
# @lc app=leetcode.cn id=2507 lang=python3
# @lcpr version=30204
#
# [2507] 使用质因数之和替换后可以取到的最小值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            s=0
            i=2
            x=n
            while i*i<=n:
                while n%i==0:
                    s+=i
                    n//=i
                i+=1
            if n>1:
                s+=n
            if s==x:
                return x
            n=s

# @lc code=end
assert Solution().smallestValue(4)==4
assert Solution().smallestValue(15)==5


#
# @lcpr case=start
# 15\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

