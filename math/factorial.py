#factorial class
class Fact:
  #factorial function with self so it has attributes of class, n is the number being entered 
    def factorial(self, n):
      #initial number we start with in a factorial   
      a = 1
#this basically calculates the value of: 1 times (given from the fact we defined a=1) all the way up until n+1 exclusive for integer values 
      for i in range(1, n+1):
        a = a*i
      return a

#input can only be integers 
n = int(input('Enter the number you want to find the factorial of:'))

#defining the object as Fact()
ob = Fact()

#a is a product of the factorial function under object Fact() with the input of n 
a = ob.factorial(n)
print("Factorial is:", a)


