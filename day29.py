#Task 1:  Middle Figure
print("\n*******************Task 1:  Middle Figure*******************")
def middle_figure(a,b):
    c = a.replace(" ", "") + b.replace(" ", "")
    mid = len(c) // 2
    print(mid)
    if mid % 2 != 0:
        return c[mid]
    else:
        return "No middle figure"

a = "make love"
b = "not wars"
result_mid = middle_figure(a,b)
print(result_mid)


