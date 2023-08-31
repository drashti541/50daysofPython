#Task 1:  Words & Special Characters
print("\n*******************Task 1:  Words & Special Characters*******************")
def  analyse_string(str1):
    l1 = []
    sc = "#$%&()'*+,-./:;<=>?@[\]^_`{|}~"
    
    for i in str1:
        if i in sc:
            l1.append(i)
            
    dict1 = {
        "Special Characters" : len(set(l1)),
        "words" : len(str1.split(" ")),
        "Total Characters" : len(str1.replace(" ", ""))
        }
    
    return dict1

str1 = "Python has a string format operator %. This functions analogously to printf format strings in C, e.g. 'spam=%s eggs=%d' % ('blah', 2) evaluates to 'spam=blah eggs=2'" 

result_word =  analyse_string(str1)
print(result_word)
