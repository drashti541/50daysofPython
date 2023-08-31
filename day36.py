#Task 1: Count String
print("\n*******************Task 1: Count String*******************")
def count(s1):
    dict1 = {}
    for i in s1:
        dict1[i] = s1.count(i)
    return dict1
  
s1 = "Hello"              
result_count= count(s1)
print(result_count)