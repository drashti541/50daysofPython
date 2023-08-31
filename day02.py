#Task 1: Strings to Integers
print("\n*******************Task 1: Strings to Integers*******************")
def convert_add(l1):
    return sum(l1)
    
l1 = []
for i in range(int(input("Enter number of elements you want to add: "))):
    l1.append(int(input("Enter parameters: ")))

int_result = convert_add(l1)
print(f"Sum of list elements:{int_result}")
 
 

#Task 2: Duplicate Names
print("\n\n*******************Task 2: Duplicate Names*******************")
def check_duplicates(l2):
    newlist, duplist = [], []
    for i in l2:
        newlist.append(i) if i not in newlist else duplist.append(i)
            
    return print(f"Duplicate: {duplist}") if len(duplist) > 0 else print("No duplicates")
        
l2 = []
for i in range(int(input("Enter number of elements you want to add: "))):
    l2.append(input("Enter string: "))
    
check_duplicates(l2)
