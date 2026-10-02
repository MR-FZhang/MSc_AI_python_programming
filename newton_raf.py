# Newton raphson approach to finding the sqaure root. 

num = int(input('Enter a number for sqaure root: '))
init_guess = 1
error = 0.0001

while abs((init_guess**2 - num)) > error:
  init_guess = (init_guess + (num/init_guess)) / 2

print(init_guess)
