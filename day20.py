#Task 1: Capitalize First Letter
print("\n*******************Task 1: Capitalize First Letter*******************")
def capitalize(s1):
    return s1.title()

s1 = input("Enter string:") #"i like learning"
result_capital = capitalize(s1)
print(result_capital)


#Task 2: Reversed List
print("\n*******************Task 2: Reversed List*******************")
def reversed_list(s2):
    l2 = []
    for i in s2.split(" "):
        if any(j.isupper() for j in i):
            l2.append(i[::-1])
    return l2

#s2 = input("Enter String: ") 
s2 = "leArning is hard, bUt if You appLy youRself\
    you can achieVe success"
result_reversed = reversed_list(s2)
print(result_reversed)
