def LSD(strs:list[str]):
    """
    Every string of the list must have same length!
    String can include any ascii code.
    """
    N=len(strs)
    if N==0:
        return strs
    L=len(strs[0])
    R=256
    for cid in range(L-1,-1,-1):
        count=[0]*R
        for i in range(N):
            count[ord(strs[i][cid])+1]+=1
        for i in range(1,R):
            count[i]+=count[i-1]
        aux=['']*N
        for i in range(N):
            _ord=ord(strs[i][cid])
            aux[count[_ord]]=strs[i]
            count[_ord]+=1
        strs=aux
    return strs

def generate_test_strs(str_len:int,str_count:int,same_str_len=True):
    import random
    strs=[]
    for _ in range(str_count):
        str=[]
        len=str_len
        if not same_str_len:
            len=random.randint(1,str_len)
        for i in range(len):
            while True:
                n=random.randint(0,127)
                ch=chr(n)
                if ch.isalnum():
                    str.append(ch)
                    break
        strs.append(''.join(str))
    return strs

def test_lsd(str_len,str_count,test_count):
    for _ in range(test_count):
        strs=generate_test_strs(str_len,str_count)
        ret=LSD(strs)
        ans=sorted(strs)
        if ret!=ans:
            raise ('Test Failed with input:',strs)
    print('Test Passed!')

if __name__ == '__main__':
    test_lsd(6,10,10)