#
# @lc app=leetcode.cn id=面试题 01.03 lang=python3
# @lcpr version=30204
#
# [面试题 01.03] URL化
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        s=list(S)
        idx=len(s)
        for i in range(length-1,-1,-1):
            ch=s[i]
            if ch==' ':
                s[idx-3:idx]='%20'
                idx-=3
            else:
                idx-=1
                s[idx]=ch
        return ''.join(s[idx:])
# @lc code=end
assert Solution().replaceSpaces("ds sdfs afs sdfa dfssf asdf             ",27)=="ds%20sdfs%20afs%20sdfa%20dfssf%20asdf"
assert Solution().replaceSpaces("Mr John Smith    ", 13)=="Mr%20John%20Smith"


#
# @lcpr case=start
# "Mr John Smith    ", 13\n
# @lcpr case=end

# @lcpr case=start
# "               ", 5\n
# @lcpr case=end

#

