num=int(input("enter the number"))
a=num%10
b=(num//10)%10
c=(num//100)%10
d=(num//1000)%10
e=(num//10000)%10
new_num=(a*10000)+(b*1000)+(c*100)+(d*10)+(e*1)
if new_num>10000:
    print(new_num)
else:
    print("invalid")
print(a,b,c,d,e)