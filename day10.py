#Task 1: Hide my Password
print("\n*******************Task 1: Hide my Password*******************")
def hide_password():
    return "*" * len(input("Enter Password: "))

hide_result = hide_password()
print(hide_result)


#Task 2: A Thousand Separator
print("\n\n*******************Task 2: A Thousand Separator*******************")
def convert_numbers(numlist):
    return [format(num, ',') for num in numlist]

numlist = [1000000, 2356989, 2354672, 9878098]
# numlist = [int(input("Enter element:"))  for i in range(int(input("Enter number of elements you want to add: ")))]

convert_result = convert_numbers(numlist)
print(convert_result)