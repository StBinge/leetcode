#
# @lc app=leetcode.cn id=面试题 05.03 lang=python3
# @lcpr version=30204
#
# [面试题 05.03] 翻转数位
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseBits(self, num: int) -> int:
        if num<0:
            num=(num & 0xffffffff)
        s=bin(num)[2:]
        ret=0
        left=0
        used=False
        for right,ch in enumerate(s):
            if ch=='0':
                if not used:
                    used=True
                else:
                    ret=max(ret,right-left)
                    while used and s[left]=='1':
                        left+=1
                    left+=1
        return min(32,max(ret,len(s)-left+(not used)))


# @lc code=end
assert Solution().reverseBits(-1)==32
assert Solution().reverseBits(1775)==8
assert Solution().reverseBits(2147483647)==32


#
# @lcpr case=start
# 1775(110111011112)\n
# @lcpr case=end

# @lcpr case=start
# 7(01112)\n
# @lcpr case=end

#

