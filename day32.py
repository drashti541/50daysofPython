#Task 1: Password Validator
print("\n*******************Task 1: Password Validator*******************")
def password_validator():
    while True:
        password = input("\nEnter password:")
        error = []
        if len(password) < 8 :
            error.append("Password should be at least 8 characters long")
        if not any(i.isupper() for i in password):
            error.append("Password should have at least one uppercase letter")
        if not any(i.islower() for i in password):
            error.append("Password should have at least one lowercase letter")
        if not any(i.isdigit() for i in password):
            error.append("Password should have at least one number" )
        
        if error:
            print("Invalid Password!!!")
            for e in error:
                print(e)
        else:
            return password
                
result_password = password_validator()
print(result_password)


#Task 2:  Valid Email
print("\n*******************Task 2:  Valid Email*******************")
def email_validator(emails):
    validemail = list(filter(lambda e: e.index("@") > 0 and e.count("@") == 1 and e.endswith(".com"), emails))

    if validemail:
        return validemail
    else:
        return "All emails are invalid"

emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com' ]
result_email = email_validator(emails)
print(result_email)