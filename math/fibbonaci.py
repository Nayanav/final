terms = int(input("Number of values in fibbonacci:"))
#first two values in fibb sequence 
n1, n2 = 0, 1

#the purpose of this is to have a value to begin with 
count = 0

#if the number of terms is less than -1, prompt user to enter a higher value 
if terms <= 0:
    print("Please enter a positive integer")

else:
  print("This is the fibbonacci sequence for the first", terms, "terms:")

#if there are more than 0 terms entered, then...
  while count < terms:

    #this is because the first value is always 0
    print(n1) 

    #in general in fibb sequence it is the   addition of the two numbers before it 
    nth = n1 + n2
    
   # switches n1 and n2 once nth is figured out so that now n2 can be updated 
    n1 = n2
    n2 = nth

  #updates count until it matches term with increasing interval of 1 
    count += 1







