#
# @lc app=leetcode.cn id=2299 lang=python3
# @lcpr version=30204
#
# [2299] 强密码检验器 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        has_lower=has_upper=has_num=has_symbol=False
        
        pre=''
        for ch in password:
            if pre==ch:
                return False
            pre=ch
            has_lower|=ch.islower()
            has_upper|=ch.isupper()
            has_num|=ch.isnumeric()
            has_symbol|=ch in '!@#$%^&*()-+'
        return has_lower & has_upper & has_num & has_symbol
# @lc code=end



#
# @lcpr case=start
# "IloveLe3tcode!"\n
# @lcpr case=end

# @lcpr case=start
# "Me+You--IsMyDream"\n
# @lcpr case=end

# @lcpr case=start
# "1aB!"\n
# @lcpr case=end

#

