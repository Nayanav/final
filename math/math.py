class Math():
  def hcf (self, a,b):

    #determine which number is smaller 
    if a > b:
     small = b

    else: 
      small = a

    #looks at numbers from 1-small+1 exclusive integers 
    for i in range (1, small+1):
        if (a % i == 0) and (b % i == 0):
          hcf = i

    return hcf

  a = int(input('Enter the first number you want to find the hcf of:'))

  b = int(input('Enter the second number you want to find the hcf of:'))

ob = Math()
hcf = ob.hcf ()
print("Factorial is:", hcf(a,b))
        
  