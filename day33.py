#Task 1: List Intersection
print("\n*******************Task 1: List Intersection*******************")
def inter_section(list1,list2):
    return tuple(sorted(set(list2).intersection(set(list1))))
  
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]                
result_section = inter_section(list1,list2)
print(result_section)


#Task 2:  Set or list
print("\n*******************Task 2:  Set or list*******************")

