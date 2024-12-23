#
# @lc app=leetcode.cn id=3114 lang=python3
# @lcpr version=30204
#
# [3114] 替换字符可以得到的最晚时间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findLatestTime(self, s: str) -> str:
        h1,h2=s[:2]
        if h1==h2=='?':
            h=str(11)
        elif h1=='?':
            if h2<'2':
                h='1'+h2
            else:
                h='0'+h2
        elif h2=='?':
            if h1=='0':
                h='09'
            else:
                h='11'
        else:
            h=h1+h2
        
        m1,m2=s[3:]
        if m1=='?':
            m1='5'
        if m2=='?':
            m2='9'
        return h+':'+m1+m2
# @lc code=end



#
# @lcpr case=start
# "1?:?4"\n
# @lcpr case=end

# @lcpr case=start
# "0?:5?"\n
# @lcpr case=end

#

