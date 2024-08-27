#
# @lc app=leetcode.cn id=1754 lang=python3
#
# [1754] 构造字典序最大的合并字符串
#

# @lc code=start
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i1=i2=0
        N1,N2=len(word1),len(word2)
        ret=[]
        while i1<N1 and i2<N2:
            if word1[i1:]>word2[i2:]:
                ret.append(word1[i1])
                i1+=1
            else:
                ret.append(word2[i2])
                i2+=1
        return ''.join(ret)+''.join(word1[i1:] if i1<N1 else word2[i2:])


# @lc code=end

assert Solution().largestMerge(word1 = "abcabc", word2 = "abdcaba")=="abdcabcabcaba"
assert Solution().largestMerge(word1 = "cabaa", word2 = "bcaaa")=="cbcabaaaaa"