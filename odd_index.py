n = int(input("enter the limit:"))
list_elements = []
for i in range(n):
    lists = int(input("enter the elements in a list:"))
    list_elements.append(lists)
for value in list_elements:
    if list_elements.index(value) % 2 != 0 :
        print(value)
