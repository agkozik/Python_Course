for i in range(7):
    print(i, end='', sep='')

print("\n---------------Reversed---------------------")

for i in reversed(range(7)):
    print(i, end='', sep='')

print("\n---------------Reversed String--------------")
str = "abcdefg"
print(str)
for i in reversed(str):
    print(i, end="")

print("\n---------------Min Max----------------------")
print(max(1, 23, 45, 4, -45))
print(min(1, 23, 45, 4, -45))
