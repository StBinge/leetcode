#
# @lc app=leetcode.cn id=1415 lang=python3
#
# [1415] 长度为 n 的开心字符串中字典序第 k 小的字符串
#

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        tot=3*pow(2,n-1)
        if tot<k:
            return ''
        k-=1
        ret=[]
        tot//=3
        ret.append('abc'[k//tot])
        k%=tot
        tot>>=1
        while tot:
            prev=ret[-1]
            if k&tot==0:
                if prev=='a':
                    ret.append('b')
                else:
                    ret.append('a')
            else:
                if prev=='c':
                    ret.append('b')
                else:
                    ret.append('c')
            # k%=tot
            tot>>=1
        return ''.join(ret)
# @lc code=end
assert Solution().getHappyString(10,100)=='abacbabacb'
assert Solution().getHappyString(2,7)==''
assert Solution().getHappyString(3,9)=='cab'
assert Solution().getHappyString(1,4)==''
assert Solution().getHappyString(1,3)=='c'
