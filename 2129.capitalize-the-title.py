#
# @lc app=leetcode.cn id=2129 lang=python3
# @lcpr version=30204
#
# [2129] 将标题首字母大写
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ret=[]
        for word in title.split(' '):
            if len(word)<=2:
                ret.append(word.lower())
            else:
                ret.append(word[0].upper()+word[1:].lower())
        return ' '.join(ret)
# @lc code=end



#
# @lcpr case=start
# "capiTalIze tHe titLe"\n
# @lcpr case=end

# @lcpr case=start
# "First leTTeR of EACH Word"\n
# @lcpr case=end

# @lcpr case=start
# "i lOve leetcode"\n
# @lcpr case=end

#

