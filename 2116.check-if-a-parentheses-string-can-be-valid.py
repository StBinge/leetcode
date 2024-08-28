#
# @lc app=leetcode.cn id=2116 lang=python3
# @lcpr version=30204
#
# [2116] 判断一个括号字符串是否有效
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N=len(s)
        if N&1:
            return False
        mx=mn=0
        for i in range(N):
            ch,bit=s[i],locked[i]
            if bit=='1':
                dif=1 if ch=='(' else -1
                mx+=dif
                mn=max(mn+dif,(i+1)%2)
            else:
                mx+=1
                mn=max(mn-1,(i+1)%2)
            if mx<mn:
                return False
        return mn==0
            



# @lc code=end



#
# @lcpr case=start
# "))()))"\n"010100"\n
# @lcpr case=end

# @lcpr case=start
# "()()"\n"0000"\n
# @lcpr case=end

# @lcpr case=start
# ")"\n"0"\n
# @lcpr case=end

#

