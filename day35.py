#Task 1: Pangram
print("\n*******************Task 1: Pangram*******************")
def check_pangram(s1):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in letters:
        if i not in s1:
            return False
    return True
  
s1 = "the quick brown fox jumps over a lazy dog"              
result_pangram = check_pangram(s1)
print(result_pangram)




#Task 2:  Find my Position
print("\n*******************Task 2:  Find my Position*******************")
def find_index(l1,num):
    listin = []
    if num in l1:
        for i in range(len(l1)):
            if l1[i] == num:
                listin.append(i)
        return listin
    else:
        for i in range(len(l1)):
            l1[i] = num
        return l1
  
l1 =  [1, 2, 4, 6, 7, 7]
num = 5            
result_index = find_index(l1,num)
print(result_index)