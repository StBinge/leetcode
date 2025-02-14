#
# @lc app=leetcode.cn id=2564 lang=python3
# @lcpr version=30204
#
# [2564] 子字符串异或查询
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        cache={}
        N=len(s)
        if (idx:=s.find('0'))>=0:
            cache[0]=[idx,idx]
        else:
            ret=[]
            for x,y in queries:
                v=x^y
                if v&(v-1):
                    ret.append([-1,-1])
                else:
                    l=v.bit_length()
                    if l>N:
                        ret.append([-1,-1])
                    else:
                        ret.append([0,v.bit_length()-1])
            return ret
        mx=max(x^y for x,y in queries)
        mx_bits=len(bin(mx))-2
        for l,ch in enumerate(s):
            if ch=='0':continue
            x=0
            for r in range(l,min(N,l+mx_bits)):
                x=(x<<1) | (ord(s[r])&1)
                if x not in cache:
                    cache[x]=[l,r]
        
        not_found=[-1,-1]
        return [cache.get(x^y,not_found) for x,y in queries]


# @lc code=end
assert Solution().substringXorQueries(s="1", queries=[[4, 5]]) == [[0, 0]]
assert Solution().substringXorQueries(s="0101", queries=[[12, 8]]) == [[-1, -1]]
assert Solution().substringXorQueries(s="101101", queries=[[0, 5], [1, 2]]) == [
    [0, 2],
    [2, 3],
]


#
# @lcpr case=start
# "101101"\n[[0,5],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# "0101"\n[[12,8]]\n
# @lcpr case=end

# @lcpr case=start
# "1"\n[[4,5]]\n
# @lcpr case=end

#
