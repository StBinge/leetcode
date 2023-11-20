#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        ret=['']*(len(s)*2)
        idx=0
        cnt=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!='-':
                ret[idx]=s[i].upper()
                idx+=1
                cnt+=1
                if cnt==k:
                    ret[idx]='-'
                    idx+=1
                    cnt=0
        if ret[idx-1]=='-':
            idx-=1
        return ''.join(reversed(ret[:idx]))
        
# @lc code=end
print(Solution().licenseKeyFormatting("r",1))
print(Solution().licenseKeyFormatting("5F3Z-2e-9-w",4))
print(Solution().licenseKeyFormatting("2-5g-3-J",2))
