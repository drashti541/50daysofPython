#Task 1: Add Under_Score
print("\n*******************Task 1: Add Under_Score*******************")
def add_hash(s1):
    return s1.replace(" " , "#")

def add_underscore(s1):
    return s1.replace("#","_")

def remove_underscore(s1):
    return s1.replace("_","")

s1 = input("Enter String:") #"Python"
print(remove_underscore(add_underscore(add_hash(s1))))

