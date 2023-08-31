#Task 1: Odd and Even
print("\n*******************Task 1: Odd and Even*******************")
def odd_even(numlist):
    even = [evennum for evennum in numlist if evennum % 2 == 0]
    odd = [oddnum for oddnum in numlist if oddnum % 2 != 0]
    return(max(even) - min(odd))

numlist = [int(input("Enter Number: ")) for i in range(int(input("Enter range of numbers you want to add: ")))]

diff_result = odd_even(numlist)
print(diff_result)



#Task 2: List of Prime Numbers
print("\n\n*******************Task 2: List of Prime Numbers*******************")
def prime_numbers(num):
    primelist = []
    
    for j in num:
        prime = True
        
        for i in range(2,j):
            if j % i == 0:
                prime = False
                break
            
        if prime:
            primelist.append(j)
            
    return primelist
            
num = range(2, int(input("Enter Number:")))
prime_result = prime_numbers(num)
print("Prime Numbers:",prime_result)