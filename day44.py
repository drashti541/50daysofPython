#Task 1:  Save Emails
print("\n*******************Task 1:  Save Emails*******************")
def save_emails():
    while True:
        email = input("Enter Email or done:")
        if email == "done":
            f.close()
            break

        with open("emails.csv","a") as f:
            f.write(f"{email}\n")
            
    a = open_emails()
    return a
        
def open_emails():
    with open("emails.csv","r") as f:
        return f.read()
  
result_email = save_emails()
print(result_email)
