#Task 1: A String Range
print("\n*******************Task 1: A String Range*******************")
def string_range(num):
    range_list = [str(i) for i in range(0,num)]
    return ".".join(range_list)

num = int(input("Enter Number: "))
range_result = string_range(num)
print(range_result)


#Task 2: Dictionary of names
print("\n\n*******************Task 2: Dictionary of names*******************")
names = [input("Enter Name: ") for i in range(int(input("Enter number of names you want to add: ")))]

dict1 = {}
for n in names:
    if n.startswith("S"):
        dict1.update({n : names.count(n)})
print(dict1)