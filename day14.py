#Task 1: Flatten the List
print("\n*******************Task 1: Flatten the List*******************")
def flat_list(list1):
    list2 = []
    for i in list1:
        for j in i:
            list2.append(j)
    return list2

list1 = [[2,4,5,6]]    
result_list = flat_list(list1)
print(result_list)


#Task 2: Teacher's Salary
print("\n\n*******************Task 2: Teacher's Salary*******************")
def your_salary():
    tname = input("Enter Teacher's Name:")
    total_periods = int(input("Enter number of periods:"))
    
    if total_periods > 100:
        over_period = total_periods - 100
        under_period = total_periods - over_period
        salary = (over_period*25) + (under_period*20)
    
    else:
        salary = total_periods * 20
    
    print("\nTeacher:", tname)
    print("Periods:", total_periods)
    print("Salary:", salary)

result_salary = your_salary()


    