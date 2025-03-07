#
# @lc app=leetcode.cn id=3302 lang=python3
# @lcpr version=30204
#
# [3302] 字典序最小的合法序列
#

# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        N=len(word1)
        suf_match=[0]*(N+1)
        M=len(word2)
        idx=M-1
        for i in range(N-1,-1,-1):
            if idx==-1:
                suf_match[i]=M
                continue
            if word1[i]==word2[idx]:
                suf_match[i]=suf_match[i+1]+1
                idx-=1
            else:
                suf_match[i]=suf_match[i+1]
        
        pre_match=[0]*(N+1)
        idx==0
        for i in range(N):
            if idx==M:
                pre_match[i+1]=M
                continue
            if word1[i]==word2[idx]:
                pre_match[i+1]=pre_match[i]+1
                idx+=1
            else:
                pre_match[i+1]=pre_match[i]
        
        # if max(pre_match[i]+suf_match[i] for i in range(N))+1<M:return []
        

        idx=0
        ret=[]
        for i in range(M):
            for j in range(97,ord(word2[i])):
                idx=word1.find(chr(j),idx)
                if idx>0 or suf_match[idx+1]+i+1>=M:
                    ret.append(idx)
                    i+=1
                    for k in range(idx+1,N):
                        if word1[k]==word2[i]:
                            ret.append(k)
                            i+=1
                    return ret
            idx=word1.find(word2[i],idx)
            ret.append(idx)
# @lc code=end
assert Solution().validSequence(word1 = "vbcca", word2 = "abc")==[0,1,2]


#
# @lcpr case=start
# "vbcca"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "bacdc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "aaaaaa"\n"aaabc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"ab"\n
# @lcpr case=end

#

