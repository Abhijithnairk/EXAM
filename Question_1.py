"""
create a new  array of dictionary by extracting data from data,json
new dictionay thus created should be as shown below


[
    {
     "name": "Organic Honeycrisp Apples Bag",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    },
    {
     "name": "Granny Smith Apples",
     "categories": ["Produce","Fruits","Apples",
     "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
     "base_price":0.64,
     "availability_status":true
    }
    .
    .
    .
    .
    
]


Remember to extract all items above illustrated are just sample
"""
import json

with open('data.json','r') as file:
    data=json.load(file)
    #print(data)
    

items = data['items']
for item in items:
   
    new_dict ={
        "name":item.get('name'),
        "categories":item.get('categories'),
        "image":item.get('image'),
        "base_price":item.get('base_price'),
        "availability_status":item.get('availability_status')
        }

    print(new_dict)
    