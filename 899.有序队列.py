#
# @lc app=leetcode.cn id=899 lang=python3
#
# [899] 有序队列
#

# @lc code=start

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1:
            ans=s
            for i in range(1,len(s)):
                ans=min(ans,s[i:]+s[:i])
            return ans
        return ''.join(sorted(s))
# @lc code=end
assert Solution().orderlyQueue("kikc",3)=="cikk"
assert Solution().orderlyQueue("enbczfjtvxerzbrvigpl",1)=="bczfjtvxerzbrvigplen"
assert Solution().orderlyQueue('cba',1)=='acb'
assert Solution().orderlyQueue('baaca',3)=="aaabc"
