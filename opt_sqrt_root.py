# Creating an optimised sqaure root algo
import math
from turtle import up
num = int(input("Input a number: "))

error = 0.00000001

def nearest_integer(num, error):
  lower_bound = 0
  upper_bound = num
  
  while abs(upper_bound - lower_bound) > error:
    mid_val = lower_bound + (upper_bound - lower_bound) / 2

    if mid_val**2 > num:
      upper_bound = mid_val
    else:
      lower_bound = mid_val
    print(upper_bound)
  return (lower_bound + upper_bound) / 2

sqaure_approx = nearest_integer(num, error)
print(sqaure_approx)
print(13.638181696985853**2)

'''
while abs(sqaure_approx - actual_root) > error:
  
  if (sqaure_approx)**2 < num:
    sqaure_approx = (sqaure_approx + error)
    print(sqaure_approx)
  elif (sqaure_approx)**2 > num:
    sqaure_approx = (sqaure_approx - error)

print(sqaure_approx)
'''