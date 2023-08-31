#Task 1: List of Tuples
print("\n*******************Task 1: List of Tuples*******************")
def make_tuples(l1,l2):
    l3 = []
    if len(l1) == len(l2):
        for i,j in zip(l1,l2):
            l3.append((i,j))
        return l3
    else:
        return f"List length is not equal"

# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
l1 = [int(input(f"Enter element{i+1}:")) for i in range(int(input("Enter list1 range:")))]
l2 = [int(input(f"Enter element{i+1}:")) for i in range(int(input("Enter list1 range:")))]

result_list = make_tuples(l1,l2)
print(result_list)


#Task 2: Even Number or Average
print("\n*******************Task 2: Even Number or Average*******************")
def even_or_average():
    numlist = [int(num) for num in input("Enter numbers separated by spaces: ").split()]
    even = []
    average = 0
    for i in numlist:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            average = sum(numlist)/len(numlist)
            
    if len(even) > 0:
        return f"Max Even Number: {max(even)}"    
    else:
        return f"Max Even Number: {average}"
    
result_num = even_or_average()
print(result_num)
