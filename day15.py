#Task 1: Same in Reverse
print("\n*******************Task 1: Same in Reverse*******************")
def same_in_reverse(str1):
    return True if str1 == str1[::-1] else False

str1 = input("Enter string:").lower()
result_reverse = same_in_reverse(str1)
print(result_reverse)

#Task 2: What’s My Age?
print("\n\n*******************Task 2: What’s My Age?*******************")
def your_age():
    names_age = {"jane": 23, 
                 "kerry": 45, 
                 "tim": 34, 
                 "peter": 27}
    
    name = input("Enter name:").lower()
    
    if name not in names_age:
        names_age[name] = input("Your name is not in the dictionary\n Enter your age:")
        print(f"Hi, {name.title()}, you are {names_age[name]} years old.")
        
    else:
        print(f"Hi, {name.title()}, you are {names_age[name]} years old.")
         
result_name = your_age()


    



    