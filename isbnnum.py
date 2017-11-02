# File: ISBN.py

# Description: This program checks if isbn numbers from a given file are valid. 

# Student Name: Mathew Perez

# Student UT EID: mjp3457

# Course Name: CS303E

# Unique Number: 51347

# Date Created: 10/28/2017

# Date Last Modified: 10/29/2017

def hasRightChars(a):
  # Ensure isbn has acceptable characters
  for i in range(0, len(a)):
    n = a[i]
    if n.isalpha():
      if (n != 'X') and (n != 'x'):
        return False
    elif (not n.isdigit()) and (not n.isalpha()):
      if (n != '-'):
        return False
  return True
  
def hasRightDig_X(a):
  # Ensure isbn has 9 digits and last char is a digit, X, or x
  last_char = a[-1:]
  if (not a.endswith("X")) and (not a.endswith("x")) and (not last_char.isdigit()):
    return False
  new_str = a.replace("-", "")
  if (len(new_str) != 10):
    return False
  return True 

def cum_sumCheck(a):
  # Remove hyphens from string
  isbn_dig = ""
  for x in a:
    d = x.replace("-", "")
    isbn_dig += d

  # Find first partial sum
  s1 = []
  sum_dig = 0
  for i in range (len(isbn_dig)):
    j = isbn_dig[i]
    if (j == "x") or (j == "X"):
      j = "10"
    sum_dig += int(j)
    s1.append(sum_dig)

  # Find second partial sum
  s2 = []
  sum_dig2 = 0
  for n in s1:
    sum_dig2 += int(n)
    s2.append(sum_dig2)
  
  # Check if last digit is divisible by 11
  if ((s2[-1]) % 11 != 0):
    return False
  return True
 
def main():
  # Open file for reading
  isbn_file = open("./isbn.txt", "r")
  isbn_str = isbn_file.read()

  # Open output file for writing
  outfile = open ("isbnOut.txt", "w")

  # Split text into list of individual isbn numbers, exclude newline characters
  new_isbn = isbn_str.splitlines()
  
  # Check conditions for valid isbn and write result to output file
  for item in new_isbn:
    if (not hasRightChars(item)):
      outfile.write (item + "  invalid\n")
          
    elif (not hasRightDig_X(item)):
      outfile.write (item + "  invalid\n")
         
    elif (not cum_sumCheck(item)):
      outfile.write (item + "  invalid\n")
     
    else:
      outfile.write (item + "  valid\n")
        
  # Close files
  isbn_file.close()
  outfile.close()

main()
