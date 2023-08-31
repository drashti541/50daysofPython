#Task 1: Sum the List
print("\n*******************Task 1: Sum the List*******************")
def sum_list(list1):
    sum1 = 0
    for i in list1:
        for j in i:
            sum1 = sum1 + j
    return sum1

list1 = [[2, 4, 5, 6], [2, 3, 5, 6]]
result_sum = sum_list(list1)
print(result_sum)


#Task 2: Unpack A Nest
print("\n\n*******************Task 2: Unpack A Nest*******************")
l1 = [[12,34,56,67],[34,68,78]]
l2 = []
for i in l1:
    for j in i:
        if j not in l2:
            l2.append(j)
print(l2[1::2])



    



    