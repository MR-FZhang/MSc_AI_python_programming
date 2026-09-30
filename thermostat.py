# A [program] to configure the temperature depending on the cu

inp_temp = float(input('Please enter temperature: '))


if inp_temp >= 20 and inp_temp <= 22:
    print('Just nice')
    print(f'New temperature: {inp_temp}')
elif inp_temp > 22.0:
    print('Too hot')
    new_temp = inp_temp - 1
    print(f'New temperature: {new_temp}')
else:
    print('Too cold')
    new_temp = inp_temp + 1
    print(f'New temperature: {new_temp}')
