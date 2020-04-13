# int_list = [1, 9, 4, 7]
# char_list = ['d', 'f', 'e', 'a']
# empty_list = []
#
# print(int_list) # [1, 9, 4, 7]
# print(char_list) # ['d', 'f', 'e', 'a']
# print(empty_list) # []
#
# list_from_range = list(range(5))
# print(list_from_range) # [0, 1, 2, 3, 4]
#
# list_from_string = list("dfhdgjfsjfsj")
# print(list_from_string) # ['d', 'f', 'h', 'd', 'g', 'j', 'f', 's', 'j', 'f', 's', 'j']

# my_list = [1, 2, 7, 4, 6, 1, 5]
# print(my_list[1])
# print(my_list[5])
#
# index = int(input("Enter an index: ")) # индекс со знаком "-" означает отсчет элемента с конца списка
# print(my_list[index])

# work with indexes my_new_list = my_list[start_index:end_index:step]
# my_list = [1, 2, 7, 4, 6, 1, 5]
# print(my_list)
# my_new_list = my_list[0:3]
# print(my_new_list)
# print(my_list[:3])
# print(my_list[0:-2])
# print(my_list[4:5])
# print(my_list[0:-1:2])
# print(my_list[::1])
# print(my_list[::-1])

# search value in the list
# my_list = [0, 1, 2, 3, 4, 4]
# value = int(input("Enter an index to search: "))
# if value in my_list:
#     print("In the List")
# else:
#     print("Not in the List")

# my_list = [0, 1, 2, 3, 4, 4]
# print("Size of myList = ", len(my_list))
#
# my_string = "a string"
# print(my_string[0])
# print(my_string[2])
# print(my_string[-1])
# print(my_string[2:6])
# print(my_string[2] + my_string[3:])
# print(len(my_string))

# create, delete, edit by index
my_list = []
my_list.append(3)
my_list.append(5)
my_list.append(my_list[0] + my_list[1])
print(my_list)
del my_list[1]
print(my_list)
my_list[0] = 1
print(my_list)

# for
my_list = [5, 4, 8, 4, 1, 3, 0]
my_new_list = sorted(my_list)
for i in my_new_list:
    print("{} ^ 2 = {}".format(i, i ** 2))
