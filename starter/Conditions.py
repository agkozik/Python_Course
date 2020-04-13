# print("""Menu:
# 1. File
# 2. View
# 3. Exit
# """)
# choice = input("Enter your choice:")
# if choice == "1":
#     print("You have selected one - File")
# elif choice == "2":
#     print("You have selected second - View")
# elif choice == "3":
#     print("You have selected third - Exit")
# else:
#     print("Sorry, incorrect choice")

# ---------------- if-else -------------------------
is_ready = True
if is_ready:
    message = "Ready"
else:
    message = "Not ready"
print(message)
# ---------------- One more ------------------------
is_ready = True
message = is_ready and "Ready" or "Not Ready"
print(message)
# ---------------- Ternary --------------------------
is_ready = True
message = "Ready" if is_ready else "Not Ready"
print(message)
print("Ready" if is_ready else "Not Ready")
# ---------------- Ternary --------------------------

new_string = input("Enter a string")
if new_string: # if string !=''
    print('The strinq is {}'.format(new_string))

number = int(input("Enter a number"))
if number:
    print(number)
else:
    print("zero")

