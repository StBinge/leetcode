#
# @lc app=leetcode.cn id=2048 lang=python3
# @lcpr version=30204
#
# [2048] 下一个更大的数值平衡数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n==0:
            return 1
        digits=[]
        _n=n
        while _n:
            digits.append(_n%10)
            _n//=10
        digits.reverse()       
        N=len(digits)     
        

        def get_upper():  
            if N==1:
                return 22
            if N<5:
                return int('1'+str(N)*N)
            if N==5:
                return 122333
            if N==6:
                return 1224444
 
        
        if n>=int(str(N)*N):
            return get_upper()
        
        ret=int(str(N)*N)
        def bulid(nums:list,idx,limit,pre):
            if idx==N:
                nonlocal ret
                if pre>n:
                    ret=min(ret,pre)
                return 
            d=digits[idx]
            start=d if limit else 1
            for i in range(start,7):
                if nums[i]:
                    nums[i]-=1
                    cur=pre*10+i
                    bulid(nums,idx+1,i==d and limit,cur)
                    nums[i]+=1
            return False
        
        nums=[0]*8
        def make_cnt(cnt,pre):
            if cnt==0:
                bulid(nums,0,True,0)
            elif cnt<=pre:
                return
            for i in range(pre+1,cnt+1):
                nums[i]+=i
                make_cnt(cnt-i,i)
                nums[i]=0

        make_cnt(N,0)
        
        return ret

# @lc code=end
assert Solution().nextBeautifulNumber(135909)==155555
assert Solution().nextBeautifulNumber(1000000)==1224444
assert Solution().nextBeautifulNumber(0)==1
assert Solution().nextBeautifulNumber(620883)==666666
assert Solution().nextBeautifulNumber(224160)==224444
assert Solution().nextBeautifulNumber(122645)==123233
assert Solution().nextBeautifulNumber(16407)==22333
assert Solution().nextBeautifulNumber(188)==212
assert Solution().nextBeautifulNumber(1000)==1333
assert Solution().nextBeautifulNumber(1)==22


#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 1000\n
# @lcpr case=end

# @lcpr case=start
# 3000\n
# @lcpr case=end

#

