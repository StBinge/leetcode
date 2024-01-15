#
# @lc app=leetcode.cn id=1108 lang=python3
#
# [1108] IP 地址无效化
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ret=['']*(len(address)+6)
        idx=0
        for c in address:
            if c!='.':
                ret[idx]=c
                idx+=1
                continue
            ret[idx]='['
            idx+=1
            ret[idx]='.'
            idx+=1
            ret[idx]=']'
            idx+=1
        return ''.join(ret)
# @lc code=end
assert Solution().defangIPaddr('1.1.1.1')=="1[.]1[.]1[.]1"
