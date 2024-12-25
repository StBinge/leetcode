#
# @lc app=leetcode.cn id=2443 lang=python3
# @lcpr version=30204
#
# [2443] 反转之后的数字和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num<20:
            if num&1==0:
                return True
        if 10<num<=99*2:
            if num%11==0:
                return True
        if 100<num<=999*2:
            for b in range(10):
                x=num-20*b
                if x<0:
                    break
                if x!=0 and x%101==0:
                    return True
        if 1000<num<=9999*2:
            for a in range(1,19):
                x=num-a*1001
                if x<0:
                    break
                if x%110==0 and 0<=x//110<=18:
                    return True
        if 10000<num<=99999:
            for a in range(1,19):
                x=num-a*10001
                if x<0:
                    break
                for b in range(19):
                    y=x-b*1010
                    if y<0:
                        break
                    if y%200==0 and y//200<=9:
                        return True
        return False

# @lc code=end
assert Solution().sumOfNumberAndReverse(99978) == False
assert Solution().sumOfNumberAndReverse(20442) == False
assert Solution().sumOfNumberAndReverse(181)
assert Solution().sumOfNumberAndReverse(0)
assert Solution().sumOfNumberAndReverse(1291)
assert Solution().sumOfNumberAndReverse(10)
assert Solution().sumOfNumberAndReverse(211) == False
assert Solution().sumOfNumberAndReverse(125) == False
assert Solution().sumOfNumberAndReverse(100) == False
assert Solution().sumOfNumberAndReverse(21) == False
assert Solution().sumOfNumberAndReverse(11)
assert Solution().sumOfNumberAndReverse(443)


#
# @lcpr case=start
# 443\n
# @lcpr case=end

# @lcpr case=start
# 63\n
# @lcpr case=end

# @lcpr case=start
# 181\n
# @lcpr case=end

#
