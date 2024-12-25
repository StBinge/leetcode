#
# @lc app=leetcode.cn id=2243 lang=python3
# @lcpr version=30204
#
# [2243] 计算字符串的数字和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        digits=list(map(int,s))
        l=len(digits)
        while l>k:
            idx=0
            for i in range(0,l,k):
                cur=sum(digits[i:min(i+k,l)])
                if cur<10:
                    digits[idx]=cur
                    idx+=1
                else:
                    digits[idx]=cur//10
                    idx+=1
                    digits[idx]=cur%10
                    idx+=1
            l=idx
        return ''.join(map(str,digits[:l]))
# @lc code=end
assert Solution().digitSum(s = "01234567890", k = 2)=='27'
assert Solution().digitSum(s = "11111222223", k = 3)=='135'


#
# @lcpr case=start
# "11111222223"\n3\n
# @lcpr case=end

# @lcpr case=start
# "00000000"\n3\n
# @lcpr case=end

#

