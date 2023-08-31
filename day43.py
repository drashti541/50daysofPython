#Task 1:  Student Marks
print("\n*******************Task 1:  Student Marks*******************")
def student_marks():
    dict1 = {}     
    while True:
        name = input("Enter Name or done:")
        if name == 'done':
            break
        marks = int(input("Enter Marks:"))
        dict1[name] = marks
    return dict1  
  
result_marks =  student_marks()
print(result_marks)
