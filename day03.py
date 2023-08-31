#Task 1: Register Check
print("\n*******************Task 1: Register Check*******************")
def register_check(register):
    stulist = [] 
    for i in register.values():
        if i == "yes":
            stulist.append(i)
    return len(stulist)
 
register = {}
for i in range(int(input("Enter number of key:value pair you want to add: "))):
    register.update({input("Enter key:"):input("Enter value:")})

register_result = register_check(register)
print(f"Number of students in school:{register_result}")




#Task 2: Lowercase Names
print("\n\n*******************Task 2: Lowercase Names*******************")
def lowercase_names(names):
    tnames = []
    for n in names:
        if n.islower():
            tnames.append(n)
    tnames.sort(reverse=True)
    return tuple(tnames)
    
names = []
for i in range(int(input("Enter number of elements you want to add: "))):
    names.append(input("Enter names: "))

lowercase_result = lowercase_names(names)
print(lowercase_result)