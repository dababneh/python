import json

data = {}
data['people'] = []
"""
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})

data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

data['people'].append({
    y : k,
})
"""
#with open('data.txt', 'w') as outfile:
    #json.dump(data, outfile)


def info1 () :
    k = int(input("Enter 0 to stop, 1 to continue: \n"))
    if k != 0:
        name1 = input("Name ")
        web1 = input("Age ")
        from1  = input("From ")
        data['people'].append({
            'name' : name1,
            'website' : web1, 
            'from' : from1,
        })
        info1()       
    else: 
        print("These are the results: ")

info1()
print(data)