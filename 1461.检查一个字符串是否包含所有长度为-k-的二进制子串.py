#
# @lc app=leetcode.cn id=1461 lang=python3
#
# [1461] 检查一个字符串是否包含所有长度为 K 的二进制子串
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        L=len(s)
        need=2**k
        edge=2**k+k-1
        if L<edge:
            return False
        n=0
        vis=set()
        vis=[False]*need
        for i in range(k):
            n=(n<<1)+int(s[i])
        vis[n]=True
        mask=(1<<k)-1
        for i in range(k,L):
            n=(n<<1)+int(s[i])
            n &=mask
            vis[n]=True
        return all(vis)
# @lc code=end
assert Solution().hasAllCodes(s = "0", k = 20)==False
assert Solution().hasAllCodes(s = "0110", k = 1)
assert Solution().hasAllCodes(s = "0110", k = 2)==False
assert Solution().hasAllCodes(s = "00110110", k = 2)
