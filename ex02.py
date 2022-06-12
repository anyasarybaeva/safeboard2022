

str=input()
str=str.split('/')
i=0
len=len(str)
while i<len:      
    if str[i]=='' or str[i]=='.':
        del str[i]
        len-=1
    elif str[i]=='..':
        del str[i]
        del str[i]
        len-=2
    else:
        i+=1

str= "/".join(str)
if list(str) ==[] or list(str)[0]!='/':
    print('/'+str)
else:
    print(str)