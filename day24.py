#Task 1: Average Calories
print("\n*******************Task 1: Average Calories*******************")
def average_calories():
    calories = []
    while True:
        intake = input("Enter calories intake or enter 'done':")
        if intake.lower() == "done":
            break
        try:
            calories.append(int(intake))
        except ValueError:
            print("Enter only number or 'done': ")
            
    if len(calories) == 0:
        return "No calory Intake"
    else:
        return f"Average: {sum(calories)/ len(calories)}"

result_multiply = average_calories()
print(result_multiply)



#Task 2: Create a Nested List
print("\n*******************Task 2: Create a Nested List*******************")
def nested_lists():
    main_list = []
    while True:
        user_list = input("Enter list numbers seprated by space or 'done' to exit): ")
        if user_list.lower() == 'done':
            break
        
        sub_list = []
        for item in user_list.split():
            sub_list.append(int(item))
        main_list.append(sub_list)
    return main_list

result_list = nested_lists()
print(result_list)