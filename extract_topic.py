import glob
import json

def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def sort_titles(data):
    sorted_data = sorted(data, key=lambda x: x['id'])
    titles = [item['title'] for item in sorted_data]
    return titles

# Find all files starting with "response" in the current directory
file_pattern = 'response_*.json'
matching_files = glob.glob(file_pattern)

# Read and process each matching file
for file_name in matching_files:
    data = read_json_file(file_name)
    sorted_titles = sort_titles(data)
    print(f"File: {file_name}")
    print("Sorted Titles:")
    for title in sorted_titles:
        print(title)
    print()
