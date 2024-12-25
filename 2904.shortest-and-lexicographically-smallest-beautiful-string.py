#
# @lc app=leetcode.cn id=2904 lang=python3
# @lcpr version=30204
#
# [2904] 最短且字典序最小的美丽子字符串
#

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        cnt=0
        ret=''
        found=False
        for i,ch in enumerate(s):
            if ch=='1':
                cnt+=1
                if cnt==k:
                    while s[left]=='0':
                        left+=1
                    if not ret or len(ret)>i-left+1:
                        ret=s[left:i+1]
                    elif len(ret)==i-left+1:
                        ret=min(ret,s[left:i+1])
                    left+=1
                    cnt-=1
                    found=True
        return ret if found else ''
# @lc code=end
assert Solution().shortestBeautifulSubstring(s = "000", k = 1)==''
assert Solution().shortestBeautifulSubstring(s = "1011", k = 2)=='11'
assert Solution().shortestBeautifulSubstring(s = "100011001", k = 3)=='11001'


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

