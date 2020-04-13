# # print 0...9
# for i in range(10):
#     print("i = ", i)
#
# # print 1...9
# for i in range(1, 10, 1):
#     print('i = ', i)

# print 10...1
# for i in range(10, 0, -1):
#     print('i = ', i)

# print from 0 to 9 with step 2 and Break
# for i in range(0, 10, 2):
#     if i == 5:
#         print("i = ", i)
#         break
#     else:
#         print("i = ", i)
# print("For ended")

# print from 0 to 10 with step 1 and Continue
# for i in range(0, 10, 1):
#     if i == 4:
#         print("Skipped value i = ", i)
#         continue
#     else:
#         print("i = ", i)
# print("For ended")

# For in Python it is Foreach, you can change i-value only in CURRENT iteration
# for i in range(5):
#     if i == 3:
#         i = i + 1
#     print(i)

# nested Loops
i = 5
for row in range(i):
    for column in range(i, 30):
        print('*', end='')
    print()