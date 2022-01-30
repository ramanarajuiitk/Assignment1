##Write a program which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
#in a comma-separated sequence on a single line.
m=2000
l=[]
while m<3201:
    if (m%7)==0 and (m%5)!=0:
        l.append(m)
    m=m+1
for i in l:
    if i==l[-1]:
        print(i,end='')
    else:
        print(i,end=',')
        