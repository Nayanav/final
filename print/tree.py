# Function to print("Tree Pattern")


#allows the input to only be an integer for width and height 
width = int(input("Width of tree   = "))
height = int(input("Height of tree = "))

#the space of the tree
space = width * height
n = 1

print("==== Chirstmas Tree Pattern====")

for x in range(1, height + 1):
    for i in range(n, width + 1):
        for j in range(space, i - 1, -1):
            print(end = ' ')
        for k in range(1, i + 1):
            print('*', end = ' ')
        print()
    n = n + 2
    width = width + 2

for i in range(1, height):
    for j in range(space - 3, -1, -1):
        print(end = ' ')
    for k in range(1, height):
        print('*', end = ' ')
    print()




  def palindrome(string):
    #looks at string backwards/reversed starting from index 0
    rstring = string[::-1]
    status = 1
    #if string does not equal to reversed string
    if(string!=rstring):
      status=0
    return status 

#input is a string 
string = input('Enter a string:')


#defining the object as Fact()
ob = Palind()
#a is a product of the factorial function under object Fact() with the input of n 
#palindrome is set to reverse string, and status equals to it 
status = ob.palindrome(string)

#if the reversed and normal strings true then palindrome 
if (status):
  print('The string you entered is a palindrome')

#if not it isn''t a palindrome 
else: 
  print('The string you entered is NOT a palindrome')