#Task 1: User Name Generator
print("\n*******************Task 1: User Name Generator*******************")
def user_name():
   return input("Enter your email: ").split('@')[0]

email_result = user_name()
print(f"Username:{email_result}")


#Task 2: Zero Both ends
print("\n\n*******************Task 2: Zero Both ends*******************")
def zeroed(num_list):
    num_list[0] , num_list[-1] = 0, 0
    return num_list

num_list = []
for i in range(int(input("Enter number of elements you want to add: "))):
    num_list.append(int(input("Enter Number:")))
    
zero_result = zeroed(num_list)
print(zero_result)
