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
##Write a Python program to accept the user's first and last name and then getting them.
##printed in the the reverse order with a space between first name and last name.
first_name=input('enter first name')
last_name=input('enter last name')
list=[last_name,' ',first_name]
for i in list:
    print(i,end='')
##Write a Python program to accept the user's first and last name and then getting them.
##printed in the the reverse order with a space between first name and last name.
pi=3.14
d=12
v=(4/3)*pi*((d/2)**3)
print(v)