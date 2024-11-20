def list_full_names(full_names):

    new_list = []

    for LastName, firstName in full_names.items():
        for name in firstName:
            new_list.append(name+ " " +LastName)
    return new_list
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']

new_dict = {"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}

for i in new_dict:
    y = 0
    print(i.keys())
    