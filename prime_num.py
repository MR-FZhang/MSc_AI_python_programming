num_up_to = int(input("Enter a number to test: "))

def identify_prime(prime_test):
  div_count = 0
  for i in range(1, prime_test + 1):
    if prime_test > 1:
      if prime_test % i == 0:
        div_count += 1
    else: 
      pass#print("Is Not a prime")

  if div_count == 2:
    print(prime_test)
  else: 
    pass
for i in range(1, num_up_to + 1):
  identify_prime(i)
