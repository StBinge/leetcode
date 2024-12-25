#
# @lc app=leetcode.cn id=2224 lang=python3
# @lcpr version=30204
#
# [2224] 转化时间需要的最少操作数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convert(s):
            hours=int(s[:2])
            minutes=int(s[3:])
            return hours*60+minutes
        
        time1=convert(current)
        time2=convert(correct)

       

        dif = time2-time1
        dif=time2-time1
        x1,dif=divmod(dif,60)
        x2,dif=divmod(dif,15)
        x3,dif=divmod(dif,5)
        return x1+x2+x3+dif

        
# @lc code=end
assert Solution().convertTime(current = "11:00", correct = "11:01")==1
assert Solution().convertTime(current = "02:30", correct = "04:35")==3


#
# @lcpr case=start
# "02:30"\n"04:35"\n
# @lcpr case=end

# @lcpr case=start
# "11:00"\n"11:01"\n
# @lcpr case=end

#

