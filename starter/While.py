# # ---------------------- while true ----------------------------
#
# message = ""
# while message != "exit":
#     message = input("Type exit to exit: ")
#
# # ---------------------- while int true ----------------------------
# n = 1
# while n <= 3:
#     print("n = ", n)
#     n += 1
#
# # ---------------------- while enter a positive number --------
# number = 0
# while number <= 0:
#     number = int(input("Enter a positive number: "))
# print("Your number is ", number)

# # ---------------------- Break --------------------------------
# i = 1
# while True:
#     print("Iterataion ", i)
#     i += 1
#     if i == 10:
#         break
# print("Loop has stopped")
# # ---------------------- Continue -----------------------------
# n = 0
# while n < 10:
#     n += 1;
#     if n == 5:
#         print("Value 5 skipped because of continue operator")
#         continue
#     print(n)
# # ---------------------- While with Else ----------------------------
attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    password = input("Please, enter Password ["
                     "you have {} attempt(s) ]: ".format(attempts_left + 1))
    if password == '1234':
        print("Correct password, signing...")
        break
else:
    print("You lost all attempts.")
