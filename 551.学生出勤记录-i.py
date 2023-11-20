#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        l_cnt=0
        a_cnt=0
        for i in range(len(s)):
            if s[i]=='A':
                a_cnt+=1
                if a_cnt>=2:
                    return False
            elif s[i]=='L':
                l_cnt+=1
                if l_cnt>=3:
                    return False
                continue

            l_cnt=0
        return True
# @lc code=end

assert Solution().checkRecord("LALL")
assert Solution().checkRecord("PPALLP")
assert Solution().checkRecord("PPALLL")==False