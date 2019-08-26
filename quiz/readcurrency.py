#!/usr/bin/env python3

import json

#write function readcurrency(filename)
# read file
#Create a dictionary 

def readcurrency(filename):
    with open(filename) as f:
        data = []
        list_data= []
        dict_data ={}
        for line in f:
            # print(line, end='')
            list_line = line.strip('\n')
            lines = list_line.split(" ")
            data.append(lines)
        
        for i in data:
            dict_data["symbole"] = i[0]
            dict_data["rate"] = i[1]
            list_data.append(dict_data)

        return list_data
    

def save(filename, data):
    with open(filename, "w") as js_file:
        new_data = {"data":data}
        json.dump(new_data,js_file, indent=2)


readcurrency("currency.txt")
save("currency.json", readcurrency("currency.txt"))
