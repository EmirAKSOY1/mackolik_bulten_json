import json

def write_json(new_data, filename='maclar.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["maclar"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

    # python object to be appended


y = {"takimlar": "Nikhil",
     "mac-tarih": "nikhil@geeksforgeeks.org",
     "MS1": "Full Time",
     "MS0": "a",
     "MS2": "xz"
     }

write_json(y)