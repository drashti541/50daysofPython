#Task 1: Division and Square-root
import math
print("\n*******************Task 1: Division and Square-root*******************")
def divide_or_square(number):
    return math.sqrt(number) if number %5 == 0 else number%5

number = int(input("Enter Number: "))
result = divide_or_square(number)
print(round(result,2))




#Task 2: Longest Value
print("\n\n*******************Task 2: Longest Value*******************")
def longest_value(dict1):
    return max(dict1.values(), key=len)
 
dict1 = {}    
for i in range(int(input("Enter number of key:value pair you want to add: "))):
    dict1.update({input("Enter key:"):input("Enter value:")})

long_result = longest_value(dict1)
print(f"Longest Value:{long_result}")

    
    