#
# @lc app=leetcode.cn id=2156 lang=python3
# @lcpr version=30204
#
# [2156] 查找给定哈希值的子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def code(ch):
            return ord(ch)-ord('a')+1
        pk=pow(power,k,modulo)
        N=len(s)
        h=0
        ret=N
        for i in range(N-1,N-k-1,-1):
            h=(h*power+code(s[i]))%modulo
        if h==hashValue:
            ret=N-k
        for i in range(N-k-1,-1,-1):
            h=(h*power+code(s[i])-code(s[i+k])*pk)%modulo
            if h==hashValue:
                ret=i
        return s[ret:ret+k]
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n7\n20\n2\n0\n
# @lcpr case=end

# @lcpr case=start
# "fbxzaad"\n31\n100\n3\n32\n
# @lcpr case=end

#

