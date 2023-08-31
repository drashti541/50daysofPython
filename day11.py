#Task 1: Are They Equal?
print("\n*******************Task 1: Are They Equal?*******************")
def equal_strings(s1,s2):
    return True if sorted(s2) == sorted(s1) else False

equal_result = equal_strings(input("Enter string1:"), input("Enter string2:"))
print(equal_result)



#Task 2: Swap Values
print("\n\n*******************Task 2: Swap Values*******************")
def swap_values(numlist):
    numlist[0], numlist[-1] = numlist[-1], numlist[0] 
    return numlist

#numlist = [2, 4, 67, 7, 10]
numlist = [ input("Enter number:") for i in range(0, int(input("Enter number of elements you want to add:"))) ]

swap_result = swap_values(numlist)
print(swap_result)