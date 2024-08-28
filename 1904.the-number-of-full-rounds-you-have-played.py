#
# @lc app=leetcode.cn id=1904 lang=python3
# @lcpr version=30204
#
# [1904] 你完成的完整对局数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        start_hour, start_minute = list(map(int, loginTime.split(":")))
        end_hour, end_minute = list(map(int, logoutTime.split(":")))
        t0=60*start_hour+start_minute
        t1=60*end_hour+end_minute
        if t0>t1:
            t1+=1440
        
        t1=t1//15*15
        return max(0,t1-t0)//15


# @lc code=end
assert Solution().numberOfRounds("09:31", "10:14") == 1
assert Solution().numberOfRounds("12:01", "12:44") == 1
assert Solution().numberOfRounds("00:47", "00:57") == 0
assert Solution().numberOfRounds("00:00", "23:59") == 95
assert Solution().numberOfRounds("20:00", "06:00") == 40


#
# @lcpr case=start
# "12:01"\n"12:44"\n
# @lcpr case=end

# @lcpr case=start
# "20:00"\n"06:00"\n
# @lcpr case=end

# @lcpr case=start
# "00:00"\n"23:59"\n
# @lcpr case=end

#
