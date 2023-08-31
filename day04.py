#Task 1: Only Floats
print("\n*******************Task 1: Only Floats*******************")
def only_floats(a, b):
    if a.isdigit() and b.isdigit():
        return 0
    elif a.isdigit() or b.isdigit():
        return 1
    else:
        return 2
    
a = input("Enter the first argument: ")
b = input("Enter the second argument: ")

float_result = only_floats(a, b)
print(f"Result: {float_result}")


#Task 2: Index of the Longest Word
print("\n\n*******************Task 2: Index of the Longest Word*******************")
def longword_index(wordlist):
    wordlen=[]
    for i in wordlist:
        wordlen.append(len(i))
        maxlen = max(wordlen)
        count = wordlen.count(maxlen)

    if count == 1:
        return wordlen.index(maxlen)
    else:
        return 0

wordlist = []
for i in range(int(input("Enter number of elements you want to add: "))):
    wordlist.append(input("Enter names: "))
longword_result = wordlist
print(longword_index(longword_result))