#Task 1: Only Words with Vowels
print("\n*******************Task 1: Only Words with Vowels*******************")
def words_with_vowels(str1):
    l2 = []
    for i in str1.split(" "):
        for j in i:
            if j in "aeiou":
                if i not in l2:
                    l2.append(i)
    return l2

str1 = "You have no rhythm"               
result_vowel = words_with_vowels(str1)
print(result_vowel)


#Task 2:  Class of Cars
print("\n*******************Task 2:  Class of Cars*******************")
class Car():
    def __init__(self, model, color, year, transmission, electric=False):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
        
    def print_cars(self):
        return f"Car Model = {self.model}\nColor = {self.color}\nYear = {self.year}\nTransmission = {self.transmission}\nElectric = {self.electric}\n"
    
class BMW(Car):
    def __init__(self, model, color, year, transmission, electric=False):
        print("********** BMW **********")
        super().__init__(model, color, year, transmission, electric= electric)

class Tesla(Car):
    def __init__(self, model, color, year, transmission, electric=False):
        print("********** TESLA **********")
        super().__init__(model, color, year, transmission, electric= electric)

class Ford(Car):
    def __init__(self, model, color, year, transmission, electric=False):
        print("********** FORD **********")
        super().__init__(model, color, year, transmission, electric= electric)



bmw1 = BMW("X6", "Silver", 2018, "Auto", False)
print(bmw1.print_cars())

tesla1 = Tesla("S", "Beige", 2017, "Auto", True)
print(tesla1.print_cars())

ford1 = Ford("Focus", "White", 2020, "Auto", False)
print(ford1.print_cars())