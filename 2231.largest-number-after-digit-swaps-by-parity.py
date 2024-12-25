#
# @lc app=leetcode.cn id=2231 lang=python3
# @lcpr version=30204
#
# [2231] 按奇偶性交换后的最大数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestInteger(self, num: int) -> int:
        x=num
        cnt=[0]*10
        while x:
            x,m=divmod(x,10)
            cnt[m]+=1

        ret=0
        for ch in str(num):
            start= (ord(ch)-ord('0')) & 1
            start+=8
            for i in range(start,-1,-2):
                if cnt[i]:
                    ret=ret*10+i
                    cnt[i]-=1
                    break
        return ret
# @lc code=end



#
# @lcpr case=start
# 1234\n
# @lcpr case=end

# @lcpr case=start
# 65875\n
# @lcpr case=end

#

