#Task 1: User Name Generator
import random
print("\n*******************Task 1: User Name Generator*******************")

def user_name():
    return input("Enter your Name:")[::-1] + str(random.randint(0, 9))

result_username = user_name()
print(result_username)


#Task 2: Sort by Length
print("\n\n*******************Task 2: Sort by Length*******************")
def sort_length(names):
    for i in range(len(names)):
        for j in range(len(names)-1):
            if len(names[j]) > len(names[j+1]):
                names[j],names[j+1] = names[j+1], names[j]
    return names

#names = [ "Peter", "Jon", "Andrew"]        
names = [input("Enter Name: ") for n in range(int(input("Enter how many elements you want to add: ")))] 

result_sort = sort_length(names)
print(result_sort)
