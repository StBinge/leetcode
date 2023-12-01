#
# @lc app=leetcode.cn id=880 lang=python3
#
# [880] 索引处的解码字符串
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size=0
        idx=-1
        for i,c in enumerate(s):
            if c.isalpha():
                size+=1
            else:
                size*=int(c)
            if size>=k:
                idx=i
                break
        for i in range(idx,-1,-1):
            k%=size
            if k==0 and s[i].isalpha():
                return s[i]
            if s[i].isalpha():
                size-=1
            else:
                size//=int(s[i])
            
# @lc code=end
S = "a2345678999999999999999"
K = 1
assert Solution().decodeAtIndex(S,K)=='a'

S = "ha22"
K = 5
assert Solution().decodeAtIndex(S,K)=='h'

S = "leet2code3"
K = 10
assert Solution().decodeAtIndex(S,K)=='o'