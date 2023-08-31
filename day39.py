#Task 1: Password Generator
import random
print("\n*******************Task 1: Password Generator*******************")
def generate_password(strength):
    if strength == "weak":
        len = 5
    elif strength == "strong":
        len = 8
    elif strength == "very strong":
        len = 12
    else:
        return "Invalid choice"
    
    ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ll = ul.lower()
    num = "1234567890"
    sym = "!@#$%^&*"
    password = "".join(random.choice(ul + sym + num + ll) for _ in range(len))
    
    return password
        
strength = input("Enter password strength(weak, strong, very strong):")       
result_guess =  generate_password(strength)
print(result_guess)
