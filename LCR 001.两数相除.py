#
# @lc app=leetcode.cn id=LCR 001 lang=python3
# @lcpr version=30204
#
# [LCR 001] 两数相除
#

import math
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def divide(self, a: int, b: int) -> int:
        sign=-1 if (a<0) ^ (b<0) else 1
        a=abs(a)
        b=abs(b)
        # if b==1:
        #     return sign*a
        ret=0
        times=1
        while a>=b+b:
            times+=times
            b+=b
        while b>0:
            while a<b:
                b>>=1
                times>>=1
            a-=b
            ret+=times
        if sign<0:
            return -ret
        return min(2**31-1,ret)
# @lc code=end
assert Solution().divide(2147483647,3)==715827882
assert Solution().divide(2147483648,1)==2147483647
assert Solution().divide(-2147483648,1)==-2147483648
assert Solution().divide(1,1)==1
assert Solution().divide(0,1)==0
assert Solution().divide(7,-3)==-2
assert Solution().divide(15,2)==7


#
# @lcpr case=start
# 15\n2\n
# @lcpr case=end

# @lcpr case=start
# 7\n-3\n
# @lcpr case=end

# @lcpr case=start
# 0\n1\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

