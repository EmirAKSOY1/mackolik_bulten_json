# Python program to read
# json file


import json

# Opening JSON file
f = open('maclar.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
print(data['maclar'][0]['MS1'])


# Closing file
f.close()
