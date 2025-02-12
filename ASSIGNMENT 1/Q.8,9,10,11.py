"""a="nana"
b=8
c=a*b
print(c, "Batman")
print("Q9")
print('Hi! we are studying \"Python\" \\n  I hope you are doing well \n we are going to have a great time!')
print("Q10")
print("Shreya Mishra \nLH-4, ITER COLLEGE \nBhubaneswar-751030")
print("Q11")
x=2
print("Value of x :",x)
print("P(x)=x^3+2x^2+3x+4","Output=",((x*x*x)+(2*x*x)+3*x+4))"""
#CHECK A NUMBER US PERFECT IS NOT
num = int(input("Enter a natural number :"))
sd = sum(i for i in range(1, num) if num % i ==0)
if sd == num:
    print(num,"Is a perfect number")
else:
    print(num,"is not a perfect number")