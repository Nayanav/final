class Palind():
  def palindrome(string):
    #looks at string backwards/reversed starting from index 0
      rstring = string[::-1]
      status=1
    #if string does not equal to reversed string
      if(string!=rstring):
          status=0
      return status
  
  #input is a string 
  string = input("Enter a string: ")

  #palindrome is set to reverse string, and status equals to it 
  status= palindrome(string)

  #if the reversed and normal strings true then palindrome 
  if(status):
      print("The string you entered is a palindrome")

#if not it isn't a palindrome 
  else:
      print("The string you entered is NOT a palindrome")
  
