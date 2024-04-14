#
# @lc app=leetcode.cn id=1513 lang=python3
#
# [1513] 仅含 1 的子串数
#

# @lc code=start
class Solution:
    def numSub(self, s: str) -> int:

        L=len(s)
        Mods=10**9+7
        ret=consecutive=0
        for ch in s:
            if ch=='0':
                ret+=(consecutive+1)*consecutive//2
                consecutive=0
            else:
                consecutive+=1
    
        return (ret+consecutive*(consecutive+1)//2)%Mods
# @lc code=end
assert Solution().numSub('0110111')==9
