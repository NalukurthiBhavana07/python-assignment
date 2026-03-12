Class Mymath :

def calculate (self, op_name,n):

if op-name = ="sum":

result = n* (n+1)/2

print("sum of first", n, "natural numbers:", result)

elifop-name = = "prime":

num = 2

Count = 0

print ("First", n, "prime numbers", end=" ")

While count<n:

is_prime = True

for i in range (2, num):

if num% i == 0:

is_prime = False

break

if is_prime:

print (num, end =" ")

Count+ = 1

num+ = 1

print()

elif op_name == "fibonacci":

a, b = 0,1

print("Fibonacci Series: ")

for i in range (n):

print (a, end= "")

a,b=b,a+b

print ()

elif op_name == "factorial":

fact = 1

for i in range (1,n+1):

fact* = i

Print("Factorial of", n," is:", fact)

else:

Print ("Invalid Operation")

math_obj= Mymath()

print("Operations: sum, prime, fibonacci, factorial")

User_op= input ("Enter Operation name:")

User_n = int (input("Enter value of n: "))

math_obj.Calculate (user_op,user_n)

