#
# @lc app=leetcode.cn id=3106 lang=python3
# @lcpr version=30204
#
# [3106] 满足距离约束且字典序最小的字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        if k==0:
            return s
        N=len(s)
        if N*25<=k:
            return 'a'*N
        ret=list(s)
        idx=0
        orda=ord('a')
        ordaa=ord('z')+1
        while k and idx<N:
            code=ord(s[idx])
            toa=min(code-orda,ordaa-code)
            if toa<=k:
                k-=toa
                ret[idx]='a'
            else:
                ret[idx]=chr(code-k)
                k=0
            idx+=1
        return ''.join(ret)

# @lc code=end
assert Solution().getSmallestString(s = "lol", k = 0)=='lol'
assert Solution().getSmallestString(s = "xaxcd", k = 4)=='aawcd'
assert Solution().getSmallestString('zbbz',3)=='aaaz'


#
# @lcpr case=start
# "zbbz"\n3\n
# @lcpr case=end

# @lcpr case=start
# "xaxcd"\n4\n
# @lcpr case=end

# @lcpr case=start
# "lol"\n0\n
# @lcpr case=end

#

