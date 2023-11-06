import os
from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

data_directory = '.'  # Directory where the JSON files are stored
read_files = set()  # Set to store the filenames of already read files

@app.route('/api/data', methods=['GET'])
def get_data():
    filename = get_next_file()  # Get the next file to read
    if filename is None:
        return jsonify({'message': 'No more files to read'})
    
    with open(filename) as file:
        # Read the file content and remove whitespace
        content = ''.join(file.read().split())
        data = json.loads(content)
    
    read_files.add(filename)  # Add the filename to the set of read files
    
    return jsonify(data)

def get_next_file():
    # Get a list of all files in the data directory
    files = os.listdir(data_directory)
    
    # Shuffle the files list to read them in a random order
    random.shuffle(files)
    
    for filename in files:
        if filename.startswith('response_') and filename not in read_files:
            return os.path.join(data_directory, filename)
    
    return None  # Return None if no more files to read

if __name__ == '__main__':
    app.run()
