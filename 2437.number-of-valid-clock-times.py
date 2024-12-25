#
# @lc app=leetcode.cn id=2437 lang=python3
# @lcpr version=30204
#
# [2437] 有效时间的数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countTime(self, time: str) -> int:
        hour,minute=time.split(':')
        ret=1
        if hour[0]==hour[1]=='?':
            ret=24
        elif hour[0]=='?':
            if hour[1]<='3':
                ret=3
            else:
                ret=2
        elif hour[1]=='?':
            if hour[0]=='2':
                ret=4
            else:
                ret=10
        

        if minute[0]=='?':
            ret*=6
        if minute[1]=='?':
            ret*=10
        return ret
# @lc code=end
assert Solution().countTime('??:??')==1440


#
# @lcpr case=start
# "?5:00"\n
# @lcpr case=end

# @lcpr case=start
# "0?:0?"\n
# @lcpr case=end

# @lcpr case=start
# "??:??"\n
# @lcpr case=end

#

