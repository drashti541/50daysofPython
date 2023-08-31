#Task 1: All the Same
print("\n*******************Task 1: All the Same*******************")
def all_the_same(arg):
   return len(set(arg)) == 1

arg = [1,1,1]
result_same = all_the_same(arg)
print(result_same)


#Task 2:  Reverse a String
print("\n*******************Task 2:  Reverse a String*******************")
def read_backwards(s1):
    return " ".join((s1.split()[::-1]))

s1 = "the love is real"
result_string = read_backwards(s1)
print(result_string)