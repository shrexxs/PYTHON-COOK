"""Define a function rotate that receives three arguments and returns a tuple in which the first argument
 is at index 1, the second argument is at index 2 and the third argument is at index 0. Define variables
 a, b and c containing ’Doug’, 22 and 1984. Then call the function three times. For each call, unpack
 its result into a, b and c, then display their values."""

def rotate(a1, b1, c1):
    return b1, c1, a1

a, b ,c ='Doug', 19, 1984

for _ in range(3):
   a, b, c =rotate(a,b,c)
   print(f"a = {a}, b = {b}, c = {c}")