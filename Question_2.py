"""
from the dictioanry thus created from question_1, 
write a program to accept a key word from  user and return a array of dictinary with item name and its the match rate


eg:

Enter keyword: Pink apple
result:[
    {
        "name": "Granny Smith Apples",
        "mathch rate":80
    }
    {
        "name": "Pink Lady Apples",
        "mathch rate":95
    }
    {
        "name": "Honey Crisp apple",
        "mathch rate":85
    }
]
match rate is percentage

match rate shown below are random not generated using program

Remember user can give any keyword in any format you have to clean it
"""

import json

keyword = input("Enter a keyword: ")

with open('data.json','r') as file:
    data=json.load(file)
    

items = data['items']
emp_list = []
for item in items:
   
    new_dict ={
        "name":item.get('name'),
        }
    #print(new_dict)
    emp_list.append(new_dict)
    
    #print(len(emp_list))
    

    

max_length = max(len(keyword), len(emp_list))

match_count = 0
for i,j in zip(keyword, emp_list):
    if i == j:
        match_count += 1
        
percentage = (match_count / max_length) * 100

print(f"The percentage of how '{keyword}' matches with '{emp_list}' is: {percentage}%")



