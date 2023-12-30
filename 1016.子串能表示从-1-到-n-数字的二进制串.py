#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] 子串能表示从 1 到 N 数字的二进制串
#

# @lc code=start
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        if n==1:
            return '1' in s
        def count(k:int,lo,hi):
            ss=set()
            num=0
            for i in range(k-1):
                num=(num<<1)+int(s[i])
            for j in range(k-1,len(s)):
                num=(num<<1)+int(s[j])
                if lo<=num<=hi:
                    ss.add(num)
                num-=(int(s[j-k+1]))<<(k-1)
            return len(ss)==hi-lo+1
        k=30
        while 1<<k >=n:
            k-=1
        if len(s)< (1<<(k-1))+k-1 or len(s)< n- (1<<k)+k+1:
            return False
        return count(k,1<<(k-1),(1<<k)-1) and count(k+1,1<<k,n)
# @lc code=end
s = "0110"
n = 4
assert not Solution().queryString(s,n)
s = "0110"
n = 3
assert Solution().queryString(s,n)