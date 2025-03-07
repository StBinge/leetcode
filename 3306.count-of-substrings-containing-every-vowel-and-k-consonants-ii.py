#
# @lc app=leetcode.cn id=3306 lang=python3
# @lcpr version=30204
#
# [3306] 元音辅音字符串计数 II
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vows='aeiou'
        ret1=ret2=left1=left2=0
        cnt1=[0]*6
        cnt2=[0]*6
        for ch in word:
            idx=vows.find(ch)
            cnt1[idx]+=1
            cnt2[idx]+=1
            while all(cnt1[:-1]) and cnt1[-1]>=k:
                cnt1[vows.find(word[left1])]-=1
                left1+=1
            ret1+=left1
            while all(cnt2[:-1]) and cnt2[-1]>k:
                cnt2[vows.find(word[left2])]-=1
                left2+=1
            ret2+=left2
        return ret1-ret2
# @lc code=end
assert Solution().countOfSubstrings(word = "ieaouqqieaouqq", k = 1)==3
assert Solution().countOfSubstrings("iqeaouqi",2)==3
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

