#Task 1: Pay Your Tax
print("\n*******************Task 1: Pay Your Tax*******************")
def your_vat():
    while True:
            inprice = input("Enter the price of the item: ")
            invat = input("Enter the VAT percentage: ")
            
            if inprice.isdigit() and invat.isdigit():
                price = float(inprice)
                vat = price * (float(invat)/100)
                total = price + vat

                return total
            else:
                print("Invalid")
        
result_vat = your_vat()
print(result_vat)


#Task 2: Pyramid of Snakes
print("\n\n*******************Task 2: Pyramid of Snakes*******************")
def python_snakes(number):
    for i in range(number):
        print(i * "\U0001f40d ")

number = int(input("Enter number:"))
result_snake = python_snakes(number)


    