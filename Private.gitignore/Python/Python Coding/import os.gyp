import os
for file in os.listdir("/Users/master"):
    if file.endswith(".txt"):
        print(os.path.join("/Users/master", file))