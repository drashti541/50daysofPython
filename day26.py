#Task 1:  Sort Words
print("\n*******************Task 1:  Sort Words*******************")
def sort_words(s1):
    return sorted(set(s1.replace(" ", "")))

s1 = "love life"
result_sort = sort_words(s1)
print(result_sort)


#Task 2:  Length of Words
print("\n*******************Task 2:  Length of Words*******************")
def string_length(s2):
    dict1  = {}
    for i in s2.split():
        dict1[i] = len(i)
    return dict1

s2 = "Hi my name is Richard"
result_string = string_length(s2)
print(result_string)