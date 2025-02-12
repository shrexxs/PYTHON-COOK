cost=float(input("enter the cost"))
print(f"Cost:{cost:.2f}")
tip = 0.18*cost
print("tip: %.2f"%(tip))
tax= 0.05*cost
print("Tax:", format(tax,'.2f'))
price = cost+ tip +tax
print("Total Price:", format(price,'.2f'))