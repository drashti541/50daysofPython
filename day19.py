#Task 1: Words and Elements
print("\n*******************Task 1: Words and Elements*******************")
def count_words(s1):
    return len(s1.split())
    

def count_elements(s1):
    return len(s1) - s1.count(" ")

s1 = input("Enter String: ") #"I love learning"
result_words = count_words(s1)
result_elements = count_elements(s1)
print(f"{result_words} Words\n{result_elements} Elements")


