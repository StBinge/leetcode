#
# @lc app=leetcode.cn id=2434 lang=python3
# @lcpr version=30204
#
# [2434] 使用机器人打印字典序最小的字符串
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def robotWithString(self, s: str) -> str:
        cnt=[0]*26
        code=lambda x:ord(x)-97
        for ch in s:
            cnt[code(ch)]+=1
        t=[]
        idx=0
        N=len(s)
        ret=[]
        mi=0
        while idx<N:
            ch=s[idx]
            t.append(ch)
            cnt[code(ch)]-=1
            idx+=1
            while mi<25 and cnt[mi]==0:
                mi+=1
            while t and code(t[-1])<=mi:
                ret.append(t.pop())
        return ''.join(ret)


# @lc code=end
assert Solution().robotWithString('bdda')=='addb'
assert Solution().robotWithString('bac')=='abc'
assert Solution().robotWithString('zza')=='azz'


#
# @lcpr case=start
# "zza"\n
# @lcpr case=end

# @lcpr case=start
# "bac"\n
# @lcpr case=end

# @lcpr case=start
# "bdda"\n
# @lcpr case=end

#

