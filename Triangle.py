#  File: Triangle.py

#  Description: This program uses four different algorithms to find the maximum path sum of a triangle of numbers.

#  Student's Name: Mathew Perez

#  Student's UT EID: mjp3457

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 03/03/2018

#  Date Last Modified:

import time

max_sum = 0

# returns the greatest path sum using exhaustive search
def exhaustive_search_help(grid, lo, row, col, sums):
  global max_sum
  hi = len(grid)
  if (lo == hi):
    if (sums > max_sum):
      max_sum = sums
  else:
    sums += grid[row][col] 
    exhaustive_search_help(grid, lo+1, row+1, col, sums)
    exhaustive_search_help(grid, lo+1, row+1, col+1, sums)

def exhaustive_search (grid):
  exhaustive_search_help(grid, 0, 0, 0, 0)
  return max_sum

# returns the greatest path sum using greedy approach
def greedy (grid):

  idx = 0
  tsum = 0
  for x in range(len(grid)):
    if x == 0:
      tsum += grid[x][0]
    else:
      if grid[x][idx] > grid[x][idx + 1]:
        tsum += grid[x][idx]
      else:
        tsum += grid[x][idx + 1]
        idx += 1
        
  return tsum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search_help (grid, row, col):
  if (row == len(grid)-1):
    return grid[row][col]
  else:
    return grid[row][col] + max(rec_search_help(grid, row+1, col), rec_search_help(grid, row+1, col+1))

def rec_search (grid):
  return rec_search_help(grid, 0, 0)


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  row = len(grid) - 1
  for y in range(len(grid)-1):
    for x in range(len(grid[row])-1):
      target = grid[row - 1][x]
      sum1 = target + grid[row][x]
      sum2 = target + grid[row][x + 1]
      if sum1 > sum2:
        grid[row - 1][x] = sum1
      else:
        grid[row - 1][x] = sum2
    row -= 1
  dp_tup = (grid[0][0], grid)
  return dp_tup

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # open file for reading
  in_file = open('./triangle.txt', 'r')
  
  # read the number of rows
  line = in_file.readline()
  line = line.strip()
  num_rows = int(line)

  # populate list with lists of rows in triangle
  grid = []
  for i in range (num_rows):
  	line = in_file.readline()
  	line = line.strip()
  	row = line.split() 
  	for i in range (len(row)):
  	  row[i] = int(row[i])
  	grid.append(row)
  
  return grid

def main ():
  # read triangular grid from file
  grid = read_file() 
  
  # Exhaustive Search
  ti = time.time()
  # output greates path from exhaustive search
  exsearch = exhaustive_search(grid)
  tf = time.time()
  del_t = tf - ti
  print()
  print("The greatest path sum through exhaustive search is", str(exsearch)+'.')
  # print time taken using exhaustive search
  print("The time taken for exhaustive search is", del_t, "seconds.")
  

  # Greedy Approach
  ti = time.time()
  # output greates path from greedy approach
  greed = greedy(grid)
  tf = time.time()
  del_t = tf - ti
  print()
  #print(greedy(grid))
  print("The greatest path sum through greedy search is", str(greed)+'.')
  # print time taken using greedy approach
  print("The time taken for greedy approach is", (del_t), "seconds.")
  
  
  # Recursive Search
  ti = time.time()
  # output greates path from divide-and-conquer approach
  rec_sum = rec_search(grid)
  tf = time.time()
  del_t = tf - ti
  print()
  print("The greatest path sum through recursive search is", str(rec_sum)+'.')
  # print time taken using divide-and-conquer approach
  print("The time taken for recursive search is", del_t, "seconds.")

  ti = time.time()
  # output greates path from dynamic programming 
  dy = dynamic_prog (grid)
  tf = time.time()
  del_t = tf - ti
  print()
  print("The greatest path sum through dynamic progamming is", str(dy[0]) + '.')
  # print time taken using dynamic programming
  print("The time taken for dynamic programming is", del_t, "seconds.")
  print()
if __name__ == "__main__":
  main()
