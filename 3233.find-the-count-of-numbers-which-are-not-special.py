#
# @lc app=leetcode.cn id=3233 lang=python3
# @lcpr version=30204
#
# [3233] 统计不是特殊数字的数字数量
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # start=math.isqrt(l)
        end=math.isqrt(r)+1
        is_prime=[0]*(end+1)
        for i in range(2,end+1):
            if is_prime[i]==0:
                is_prime[i]=is_prime[i-1]+1
                for j in range(i+i,end+1,i):
                    is_prime[j]=-1
            else:
                is_prime[i]=is_prime[i-1]

        return r-l+1 - (is_prime[math.isqrt(r)]-is_prime[math.isqrt(l-1)])
        
# @lc code=end
assert Solution().nonSpecialCount(1,2)==2
assert Solution().nonSpecialCount(4,16)==11
assert Solution().nonSpecialCount(5,7)==3


#
# @lcpr case=start
# 5\n7\n
# @lcpr case=end

# @lcpr case=start
# 4\n16\n
# @lcpr case=end

#

