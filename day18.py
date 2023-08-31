#Task 1: Any Number of Arguments
print("\n*******************Task 1: Any Number of Arguments*******************")
def any_number(*arg):
    return sum(arg)/len(arg)

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
    
result_avg = any_number(*numbers)
print(result_avg)

#Task 2: : Add and Reverse
print("\n\n*******************Task 2: : Add and Reverse*******************")
def add_reverse(list1,list2):
    if len(list1) == len(list2):
        list3 = [i+j for i,j in zip(list1,list2)]
        list3.sort(reverse=True)
        return list3
    else:
        return f"The lists are not of equal lengths"

# list1 = [10,12,34,1]
# list2 = [12,56,78,1]
list1 = [int(input(f"Enter element{i+1}:")) for i in range(int(input("Enter list1 range:")))]

list2 = [int(input(f"Enter element{i+1}:")) for i in range(int(input("Enter list2 range:")))]

    
result_add = add_reverse(list1,list2)
print(result_add)


