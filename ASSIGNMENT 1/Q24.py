d1=(int)(input("enter first integer"))
d2=(int)(input("enter second integer"))
d3=(int)(input("enter third integer"))
l=max(max(d1,d2),d3)
s=min(min(d1,d2),d3)
m=(d1+d2+d3)-l-s
print("The Sorted Order:" ,l,m,s)