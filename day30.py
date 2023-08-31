#Task 1: Most Repeated Name
print("\n*******************Task 1: Most Repeated Name*******************")
def repeated_name(name):
    repeat = {}
    for i in name:
        repeat[name.count(i)] = i

    return repeat[max(repeat)]

name = ["John", "Peter", "John", "Peter", "Jones", "Peter","John","John","Peter","Peter"]
result_name = repeated_name(name)
print(result_name)


#Task 2:  Sort by Last Name
print("\n*******************Task 2:  Sort by Last Name*******************")
def sorted_names(names):
    newname= []
    for i in names:
        newname.append(" ".join((i.split()[::-1])))
    return sorted(newname)

names = ["Beyonce Knowles", "Alicia Keys", "Katie Perry", "Chris Brown","Tom Cruise"]
result_string = sorted_names(names)
print(result_string)