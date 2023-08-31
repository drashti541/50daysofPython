#Task 1: Biggest Odd Number
print("\n*******************Task 1: Biggest Odd Number*******************")
def biggest_odd(num):
    oddlist = [int(i) for i in num if int(i) % 2 != 0]
    return max(oddlist) if oddlist else None

num = input("Enter Number:")
bigodd_result = biggest_odd(num)
if bigodd_result is not None:
    print(bigodd_result)
else:
    print("No odd numbers")


#Task 2: Zeros to the End
print("\n\n*******************Task 2: Zeros to the End*******************")
def zeros_last(numlist):
    zerolist = []
    for i in numlist:
        if i == 0:
            zerolist.append(i)
            numlist.remove(i)
    
    return sorted(numlist) + zerolist if zerolist else sorted(numlist)
 
numlist = [int(input("Enter element:"))  for i in range(int(input("Enter number of elements you want to add: ")))]

zero_result = zeros_last(numlist)
print(zero_result)