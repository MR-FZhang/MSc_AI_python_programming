# Check whether an input year is a leap year

leap_test = int(input('input a year to test: '))

if leap_test%100 == 0 and leap_test%400 == 0:
    print('Leap year')

elif leap_test%4 == 0 and leap_test%100 != 0:
    print('Leap year')

else:
    print('Not a leap year')
