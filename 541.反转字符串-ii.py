#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ret=list(s)
     
        for i in range(0,len(s),2*k):
            ret[i:i+k]=reversed(s[i:i+k])
        
        return ''.join(ret)
                
# @lc code=end
assert Solution().reverseStr('abcdefg',2)=="bacdfeg"
assert Solution().reverseStr('abcd',2)=="bacd"
