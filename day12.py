import datetime
#Task 1:  Count the Dots
print("\n*******************Task 1:  Count the Dots*******************")
def count_dots(s1):
    return s1.count(".") 

equal_result = count_dots(input("Enter String:"))
print(equal_result)



#Task 2: Your Age in Minutes
print("\n\n*******************Task 2: Your Age in Minutes*******************")
def age_in_minutes():
    while True:
        birthyear = input("Enter your Birth Year: ")
        
        if len(birthyear) != 4 or not birthyear.isdigit():
            print("Invalid Input!!! Enter four digit year")
            continue
        
        birthyear = int(birthyear)
        currentyear = datetime.datetime.now().year
        
        if birthyear < 1900:
            print("Invalid input!!! Enter valid year")
            
        elif birthyear > currentyear:
            print("Invalid input!!! Enter valid year")
            
        else:
            age_result = (currentyear - birthyear) * 365 * 24 * 60
            return age_result

age_result = age_in_minutes()
print(f"You are {format(age_result,',')} minutes old.")
    