#
# @lc app=leetcode.cn id=1849 lang=python3
#
# [1849] 将字符串拆分为递减的连续值
#


# @lc code=start
class Solution:
    def splitString(self, s: str) -> bool:
        N = len(s)
        
        initial=0
        for i in range(N-1):
            initial=initial*10+int(s[i])
            target=initial-1
            if target==0:
                if all(s[k]=='0' for k in range(i+1,N)):
                    return True
                else:
                    continue
            nxt=0
            for j in range(i+1,N):
                if target==0:
                    if all(s[k]=='0' for k in range(j,N)):
                        return True
                    else:
                        break
                nxt=nxt*10+int(s[j])
                if nxt==target:
                    if j==N-1:
                        return True
                    target-=1
                    nxt=0
        return False


# @lc code=end
assert Solution().splitString("200100") == True
assert Solution().splitString("10") == True
assert Solution().splitString("10009998") == True
assert Solution().splitString("9080701") == False
assert Solution().splitString("050043") == True
assert Solution().splitString("1234") == False
