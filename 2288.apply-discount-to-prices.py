#
# @lc app=leetcode.cn id=2288 lang=python3
# @lcpr version=30204
#
# [2288] 价格减免
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        ret=[]
        discount=(100-discount)/100
        for word in sentence.split(' '):
            if word[0]!='$' or len(word)==1:
                ret.append(word)
                continue
            num=0
            for ch in word[1:]:
                if not ch.isnumeric():
                    ret.append(word)
                    break
                num=num*10+int(ch)
            else:
                ret.append(f'${num*discount:.2f}')
        return ' '.join(ret)
# @lc code=end
assert Solution().discountPrices(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50)=="there are $0.50 $1.00 and 5$ candies in the shop"


#
# @lcpr case=start
# "there are $1 $2 and 5$ candies in the shop"\n50\n
# @lcpr case=end

# @lcpr case=start
# "1 2 $3 4 $5 $6 7 8$ $9 $10$"\n100\n
# @lcpr case=end

#

