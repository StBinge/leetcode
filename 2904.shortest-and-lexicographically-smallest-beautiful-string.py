#
# @lc app=leetcode.cn id=2904 lang=python3
# @lcpr version=30204
#
# [2904] 最短且字典序最小的美丽子字符串
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cnt=0
        l=0
        ret=''
        mi_len=len(s)+1
        for r,ch in enumerate(s):
            if ch=='1':
                cnt+=1
                if cnt==k:
                    while s[l]=='0':
                        l+=1
                    L=r-l+1
                    if L<mi_len:
                        mi_len=L
                        ret=s[l:r+1]
                    elif L==mi_len:
                        ret=min(ret,s[l:r+1])
                    l+=1
                    cnt-=1
        return ret
# @lc code=end
assert Solution().shortestBeautifulSubstring('100011001',3)=='11001'


#
# @lcpr case=start
# "100011001"\n3\n
# @lcpr case=end

# @lcpr case=start
# "1011"\n2\n
# @lcpr case=end

# @lcpr case=start
# "000"\n1\n
# @lcpr case=end

#

