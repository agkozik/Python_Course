number = int(input('Enter a number: '))
if number > 5:
    print("This number is bigger then 5.")
else:
    print("This number is less then 5.")
print("----------------------------------------")

name = 'Sasha'
if name == 'Sasha':
    print('Hello,', name)
else:
    print('What is your name?')
    name = input("Enter your name.")
    print('Hello,', name)
print("----------------------------------------")

x = float(input("x = "))

if 0 < x < 7:
    print('0 < x < 7')
    y = 2 * x - 5
    if y < 0:
        print('y < 0')
    elif y > 0:
            print('y > 0')
    else:
         print('y = 0')
print("----------------------------------------")