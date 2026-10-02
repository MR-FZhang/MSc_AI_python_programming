import math
num = int(input("Input a number: "))

actual_root = math.sqrt(num)

error = 0.0000001

sqaure_approx = 5.231445654


while abs(sqaure_approx - actual_root) > error:
  if (sqaure_approx)**2 < num:
    sqaure_approx = (sqaure_approx + error)
    print(sqaure_approx)
  elif (sqaure_approx)**2 > num:
    sqaure_approx = (sqaure_approx - error)

print(sqaure_approx)
