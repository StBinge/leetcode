#
# @lc app=leetcode.cn id=1864 lang=python3
#
# [1864] 构成交替字符串需要的最小交换次数
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        N=len(s)
        cnt1=s.count('1')
        cnt0=s.count('0')
        if min(cnt1,cnt0)!=N//2:
            return -1
        if N&1:
            ch='0'
            if cnt1>cnt0:
                ch='1'
            return sum(s[i]!=ch for i in range(0,N,2))
        else:
            r=sum(s[i]!='0' for i in range(0,N,2))
            return min(r,N//2-r)

# @lc code=end
assert Solution().minSwaps('111000')==1
assert Solution().minSwaps('111000')==1
