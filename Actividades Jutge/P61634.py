año=int(input())
if año%4==0 and año%100!=0:
    print("YES")
elif año%400==0:
    print("YES")
else:
    print("NO")