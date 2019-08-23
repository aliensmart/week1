
# Write a function `req_to_json(filename)` 

# that takes in the name of a `requirements.txt` file

# and converts it to json.

import json

def req_to_json(filename):
    with open(filename, 'r') as file_object:
        lines = file_object.readlines()
        # print(lines)
        dictionary = {}
        for line in lines:
            line = line.split('==')
            # print(line)
            dictionary[line[0]] = line[1]
    return dictionary

def save_json(dictionary):
    with open('requirements.json', 'w') as file_object:
        json.dump(dictionary, file_object, indent=2)


save_json(req_to_json('requirements.txt'))