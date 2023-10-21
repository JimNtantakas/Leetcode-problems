def reverse(x):
    new_num=''
    lim=-1
    string=str(x)
    if string[0]=='-':
        new_num+='-'
        lim=0
    new_num+=string[len(string)-1]
    for i in range(len(string)-2,lim,-1):
        new_num+=string[i]
    final=int(new_num)
    if final<-2**31 or final>(2**31)-1:
        return 0
    return  final