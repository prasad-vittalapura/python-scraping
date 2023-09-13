import json


# Define a function to traverse the JSON data
def traverse_json(data):
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"Key: {key}")
            traverse_json(value)
    elif isinstance(data, list):
        for item in data:
            traverse_json(item)
    else:
        print(f"Value: {data}")

# Start traversing from the top-level JSON object
