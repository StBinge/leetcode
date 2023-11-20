#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret=0
        L=len(s)
        left,right=0,0
        count=[0]*26
        ordA=ord('A')
        maxn=0
        while right<L:
            idx=ord(s[right])-ordA
            count[idx]+=1
            maxn=max(maxn,count[idx])
            if (right-left+1-maxn)>k:
                lidx=ord(s[left])-ordA
                count[lidx]-=1
                left+=1
            right+=1

        return right-left
# @lc code=end

assert Solution().characterReplacement('AABABBA',1)==4
assert Solution().characterReplacement('ABAA',0)==2
assert Solution().characterReplacement('ABAB',2)==4