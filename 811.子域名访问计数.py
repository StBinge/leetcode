#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#
from typing import List
# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt={}
        for cp in cpdomains:
            v,domain=cp.split(' ')
            v=int(v)
            # for i in range(len(domain)-1,-1,-1):
            cnt[domain]=cnt.get(domain,0)+v
            parts=domain.split('.')
            for i in range(1,len(parts)):
                key='.'.join(parts[i:])
                cnt[key]=cnt.get(key,0)+v
        return [f'{v} {k}' for k,v in cnt.items()]
# @lc code=end
cpdomains = ["9001 discuss.leetcode.com"]
print(Solution().subdomainVisits(cpdomains))
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(Solution().subdomainVisits(cpdomains))