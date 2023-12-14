#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#
from sbw import *
# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ret=set()
        for email in emails:
            name=[]
            append=True
            for i,c in enumerate(email):
                if c=='@':
                    ret.add(''.join(name)+email[i:])
                    break
                if c=='.':
                    continue
                elif c=='+':
                    append=False
                elif append:
                    name.append(c)
        return len(ret)
# @lc code=end
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
assert Solution().numUniqueEmails(emails)==3

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
assert Solution().numUniqueEmails(emails)==2
