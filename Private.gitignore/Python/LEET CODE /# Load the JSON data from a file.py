import json

# Load the JSON data from a file
with open("/Users/jamildababneh/Desktop/Personal /Python/LEET CODE /avengers.json", "r") as f:
    data = json.load(f)

# Create a list of Avenger objects from the JSON data
avenger_list = [item for item in data]

for item in avenger_list:
    print(item["rating"])





