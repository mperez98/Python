#  File: Grid.py

#  Description: This program prints the greatest product of four adjacent numbers in the same direction in a grid of positive integers from a text file.

#  Student Name: Mathew Perez

#  Student UT EID: mjp3457

#  Course Name: CS 303E

#  Unique Number: 51347

#  Date Created: 11/01/17

#  Date Last Modified: 11/01/17

def main():
  # Open file for reading
  in_file = open("./grid.txt", "r")

  # Read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int(dim)

  # Create an empty grid
  grid = []

  # Populate the grid
  for i in range (dim):
    line = in_file.readline()
    row = line.split()
    for j in range (dim):
      row[j] = int (row[j])
    grid.append(row)

  # Establish max values to be replaced
  max_horizontal, max_vertical, max_ldiag, max_rdiag = 0, 0, 0, 0
  
  # Find greatest product of four numbers in a row
  for row in grid:
    for i in range (dim-3):
      h_prod = 1
      for j in range (i, i+4):
        h_prod = h_prod * row[j]
        if (h_prod > max_horizontal):
          max_horizontal = h_prod

  # Find greatest product of four numbers in a column
  for j in range (dim):
    for i in range (dim-3):
      v_prod = 1
      for k in range (i, i+4):
        v_prod = v_prod * grid[k][j]
        if (v_prod > max_vertical):
          max_vertical = v_prod

  # Find greatest product of four numbers in L to R diagonal
  for i in range (dim-3):
    for j in range (dim-3):
      ldiag_prod = 1
      for k in range (4):
        ldiag_prod = ldiag_prod * grid[i+k][j+k]
        if (ldiag_prod > max_ldiag):
          max_ldiag = ldiag_prod

  # Find greatest product of four numbers in R to L diagonal
  for i in range (dim-3):
    for j in range (3, dim):
      rdiag_prod = 1
      for k in range (4):
        rdiag_prod = rdiag_prod * grid[i+k][j-k]
        if (rdiag_prod > max_rdiag):
          max_rdiag = rdiag_prod

  # Find largest product of four numbers
  largest_prods = [max_horizontal, max_vertical, max_ldiag, max_rdiag]
  max_prod = max(largest_prods)

  # Close file
  in_file.close()

  # Display result
  print("The greatest product is", str(max_prod) + ".")

main()
