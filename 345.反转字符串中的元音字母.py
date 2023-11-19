#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        ss=list(s)
        N=len(s)
        l,r=0,N-1

        vowels='AEIOUaeiou'
        while l<r:
            while l<N and s[l] not in vowels:
                l+=1
            while r>-1 and s[r] not in vowels:
                r-=1
            if l<r:
                ss[l],ss[r]=ss[r],ss[l]
                l+=1
                r-=1
        return ''.join(ss)

# @lc code=end
assert Solution().reverseVowels('hello')=='holle'
assert Solution().reverseVowels('leetcode')=='leotcede'
assert Solution().reverseVowels('aA')=='Aa'
