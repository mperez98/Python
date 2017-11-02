#  File: Hailstone.py

#  Description: This program prints the longest Hailstone cycle length in a given range of numbers

#  Student Name: Mathew Perez

#  Student UT EID: mjp3457

#  Course Name: CS 303E

#  Unique Number: 51347

#  Date Created: 09/28/2017

#  Date Last Modified: 09/29/2017

def main():
  # Prompt user to input start and end numbers
  a = int(input("Enter starting number of the range: "))
  print()
  b = int(input("Enter ending number of the range: "))

  # Check if both inputs are positive and second number is greater than first number
  while (a <= 0) or (b <= 0) or (a >= b):
    a = int(input("Enter starting number of the range: "))
    print()
    b = int(input("Enter ending number of the range: "))
  
  # Compute Hailstone sequence of given range
  cycleLength = 0
  max_num = 0
  for n in range (a, b + 1):
    counter = 0
    i = n
    while (i != 1):
      if (i % 2 == 0):
        i = i // 2
        counter += 1
      else:
        i = 3 * i + 1
        counter += 1 
    
    # Update cycleLength and max_num
    if (counter >= cycleLength): 
      cycleLength = counter
      max_num = n
  
  # Display result
  print()
  print("The number", max_num, "has the longest cycle length of", str(cycleLength) + '.')
main()


