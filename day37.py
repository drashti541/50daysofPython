#Task 1: Count the Vowels
print("\n*******************Task 1: Count the Vowels*******************")
def count_the_vowels(s1):
    list_result = []
    vowels = "aeiouAEIOU"
    for i in s1:
        if i in vowels:
            list_result.append(i)
    return f"{len(set(list_result))} vowels"
  
s1 = "Hello"              
result_count= count_the_vowels(s1)
print(result_count)