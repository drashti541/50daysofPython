#Task 1: Pig Latin
print("\n*******************Task 1: Pig Latin*******************")
def translate(a):
    l1 = []
    v = "aeiou"
    for i in (a.split(" ")):
        if i[0].lower() in v:
            l1.append(i + "yay")
        else:
            l1.append(i[1:] +i[0] + "ay") 
    return " ".join(l1)
        
a = "i love python"     
result_translate =  translate(a)
print(result_translate)
