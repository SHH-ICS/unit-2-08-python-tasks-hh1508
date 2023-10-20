# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.

# Returns a string that is the contents of the myName variable written backwards
# ie: passing Atkinson as the parameter would return nosniktA
def reverseName(myName):
  myName = 'Haley'
   myName[::-1]
    nameLength=len(myName)
    slicedName=myName[nameLength::-1]
    print(slicedName)
  result = myName
  return result

# Returns a float value that is the contents of the myAge variable square rooted
# ie: passing 16 as the parameter would return 4.0
def rootAge(myAge): 
  # Write your code here
import math.sqrt()
myAge=int(input())
   print(math.sqrt(myAge))
  result = myAge
  return result
