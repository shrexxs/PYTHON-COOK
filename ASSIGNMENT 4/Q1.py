"""Write a Python program to create a list of size N and store the random values in it and find the sum
and average."""
import random

def random_list(size):
    
    ran_l = [random.randint(1, 100) for _ in range(size)]
    total = sum(ran_l) 
    avg = total / size if size > 0 else 0  
    return ran_l, total, avg

N = int(input("Enter the size of the list: "))
ran_l, total, avg = random_list(N)
print(f"Random List: {ran_l}")
print(f"Sum: {total}")
print(f"Average: {avg}")
