#Task 1: My Discount
print("\n*******************Task 1: My Discount*******************")
def my_discount():
    price = int(input("Enter Price: "))
    discount = int(input("Enter Discount Percentage: "))
    return price- (price * (discount/100))

discount_result = my_discount()
print(discount_result)


#Task 2: Tuple of Student Sex
print("\n\n*******************Task 2: Tuple of Student Sex*******************")
def student_gender(studentlist):
    list3= [
    ("Male", 
     (studentlist.count("male") + studentlist.count("Male"))),
    ("Female", 
     (studentlist.count("female") + studentlist.count("Female")))]  
    return list3

studentlist=[]
for i in range(int(input("Enter number of students you want to add:"))):
    studentlist.append(input("Enter Gender:"))

student_result = student_gender(studentlist)
print(student_result)