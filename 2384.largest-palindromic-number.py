#
# @lc app=leetcode.cn id=2384 lang=python3
# @lcpr version=30204
#
# [2384] 最大回文数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt=[0]*10

        for n in num:
            cnt[int(n)]+=1

        if cnt[0]==len(num):
            return '0'
        ret=''
        for i in range(9,0,-1):
            ret+=str(i)*(cnt[i]//2)

        if ret:
            ret+='0'*(cnt[0]//2)

        for i in range(9,-1,-1):
            if cnt[i]&1:
                return ret+str(i)+ret[::-1]
        return ret+ret[::-1]

# @lc code=end
assert Solution().largestPalindromic('00001105')=='1005001'
assert Solution().largestPalindromic('00011')=='10001'
assert Solution().largestPalindromic('00000')=='0'
assert Solution().largestPalindromic('00009')=='9'
assert Solution().largestPalindromic('444947137')=='7449447'


#
# @lcpr case=start
# "444947137"\n
# @lcpr case=end

# @lcpr case=start
# "00009"\n
# @lcpr case=end

#

