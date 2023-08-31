#Task 1: Longest Word
print("\n*******************Task 1: Longest Word*******************")
def longest_word(words):
    return [len(max(words, key=len)), max(words, key=len)]

words =  ["Java", "JavaScript", "Python"]
result_long = longest_word(words)
print(result_long)


#Task 2:  Create User
print("\n*******************Task 2:  Create User*******************")
def create_user():
    user_dict = {
        "name" : input("Enter Name:"),
        "age" : int(input("enter age:")),
        "password" : input("Enter password:")
    }
    print("User saved. Please login")
    
    while True:
        name = input("Enter your Name:")
        password = input("Enter password:")
        
        if name == user_dict["name"] and password == user_dict["password"]:
            return "Logged in successfully"
        
        else:
            print("Wrong password or user name. Please try again")

result_string = create_user()
print(result_string)