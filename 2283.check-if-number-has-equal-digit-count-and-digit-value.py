#
# @lc app=leetcode.cn id=2283 lang=python3
# @lcpr version=30204
#
# [2283] 判断一个数的数字计数是否等于数位的值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def digitCount(self, num: str) -> bool:
        cnt=[0]*10
        for n in num:
            cnt[ord(n)-ord('0')]+=1
        return all(int(num[i])==cnt[i] for i in range(len(num)))
# @lc code=end
assert Solution().digitCount('1210')


#
# @lcpr case=start
# "1210"\n
# @lcpr case=end

# @lcpr case=start
# "030"\n
# @lcpr case=end

#

