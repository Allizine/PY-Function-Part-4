#Max-Number
def max_num(x,y,z):
    return max([x,y,z])
#Multi-List 
def multi_list(lst):
  if len(lst) == 0:
    return 0
  prod = lst[0]
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i
  return prod
#Rev_String 
def rev_string(my_str):
    return my_str[::-1]
#number_within
def number_within(a,b,c):
    return a in range(b,c+1)
#pascal
triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1
    for row in triangle:
      print(row)
