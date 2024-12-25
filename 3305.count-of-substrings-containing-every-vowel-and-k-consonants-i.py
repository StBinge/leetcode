#
# @lc app=leetcode.cn id=3305 lang=python3
# @lcpr version=30204
#
# [3305] 元音辅音字符串计数 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N=len(word)
        vows='aeiou'

        cnt1=defaultdict(int)
        cnt2=defaultdict(int)

        left1=left2=0
        k1=k2=0

        ret=0
        for b in word:
            if b in vows:
                cnt1[b]+=1
                cnt2[b]+=1
            else:
                k1+=1
                k2+=1

            while len(cnt1)==5 and k1>=k:
  
                pre=word[left1]
                if pre in vows:
                    if cnt1[pre]==1:
                        del cnt1[pre]          
                    else:
                        cnt1[pre]-=1
                else:
                    k1-=1
                left1+=1

            while len(cnt2)==5 and k2>=k+1:
       
                pre=word[left2]
                if pre in vows:
                    if cnt2[pre]==1:
                        del cnt2[pre]          
                    else:
                        cnt2[pre]-=1
                else:
                    k2-=1
                left2+=1
            ret+=left1-left2
        return ret
        
# @lc code=end
assert Solution().countOfSubstrings(word = "ieaouqqieaouqq", k = 1)==3
assert Solution().countOfSubstrings(word = "aeiou", k = 0)==1
assert Solution().countOfSubstrings(word = "aeioqq", k = 1)==0


#
# @lcpr case=start
# "aeioqq"\n1\n
# @lcpr case=end

# @lcpr case=start
# "aeiou"\n0\n
# @lcpr case=end

# @lcpr case=start
# "ieaouqqieaouqq"\n1\n
# @lcpr case=end

#

