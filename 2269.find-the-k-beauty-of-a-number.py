#
# @lc app=leetcode.cn id=2269 lang=python3
# @lcpr version=30204
#
# [2269] 找到一个数字的 K 美丽值
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        x=int(s[:k])
        ret=int(num%x==0)
        hi=10**(k-1)
        for i in range(k,len(s)):
            x%=hi
            x=x*10+int(s[i])
            if x!=0 and num%x==0:
                ret+=1
        return ret
# @lc code=end
assert Solution().divisorSubstrings(2,1)==1
assert Solution().divisorSubstrings(430043,2)==2
assert Solution().divisorSubstrings(240,2)==2


#
# @lcpr case=start
# 240\n2\n
# @lcpr case=end

# @lcpr case=start
# 430043\n2\n
# @lcpr case=end

#

