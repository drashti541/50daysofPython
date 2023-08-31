#Task 1:  Save a JSON
print("\n*******************Task 1:  Save a JSON*******************")
import json
names = {'name': 'Carol','sex': 'female','age': 55}
def save_json(dict1):
    with open('file.json', 'w') as my_file:
        json.dump(dict1, my_file, indent=4)   
save_json(names)

def read_json():
    with open('file.json', 'r') as my_file:
        json_file = json.load(my_file)
    return json_file
print(read_json())
