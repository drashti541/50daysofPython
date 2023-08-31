#Task 1:  Unique Numbers
print("\n*******************Task 1:  Unique Numbers*******************")
def unique_numbers(original_list):
    unique_list = sorted(set(original_list))
    
    if (sum(original_list) - sum(unique_list)) % 2 == 0:
        return original_list
    else:
        return unique_list

original_list = [1, 2, 4, 5, 6, 7, 8, 8]
result_unique = unique_numbers(original_list)
print(result_unique)


#Task 2:  Difference of two Lists
print("\n*******************Task 2:  Difference of two Lists*******************")
def difference(list1, list2):
    dif1 = [x for x in list1 if x not in list2]
    dif2 = [x for x in list2 if x not in list1]
    return dif1+dif2

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
result_difference = difference(list1 , list2)
print(result_difference)