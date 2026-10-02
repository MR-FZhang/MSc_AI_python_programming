num_star = int(input("input the number of stars: "))
counter = 1
row = 0
while counter <= num_star:
  print((1+(2*row))*'*')
  counter += 1
  row += 1