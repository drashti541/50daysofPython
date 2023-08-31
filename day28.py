#Task 1:  Return Indexes
print("\n*******************Task 1:  Return Indexes*******************")
def index_position(s1):
    return [s1.index(i) for i in s1 if i.islower()]

s1 = "LovE"
result_index = index_position(s1)
print(result_index)


#Task 2:  Largest Number
print("\n*******************Task 2:  Largest Number*******************")
def largest_number(list1):
    s = ""
    for i in list1:
        s = s + str(i)
    num = "".join(sorted(s,reverse = True))
    return format(int(num),",")

list1 = [3, 67, 87, 9, 2]
result_large = largest_number(list1)
print(result_large)