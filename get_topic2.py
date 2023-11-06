from bardapi import Bard, SESSION_HEADERS
import os
import requests
import json
import random
from datetime import datetime

# Set token
token = '' #set bard api token here

# Set session
session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token)

# Accept user input for the input text
input_text = "I want you to act as a professional blog writer. Write down a story telling type of blog post about this topic :1. SME, 2.artifical intelligence, 3.marketing, 4.branding, 5.route to market, 6.warhouse management, 7.inventory system, 8.recommendation, 9.price analysis, 10.market analysis and 11.all topic related to brands and 12. business) - choose one topic only use professional tone, make it SEO-friendly, ensure it's not plagiarsm, be creative. Make it engaging and fun to read. use markdown format inside html tag"

# Give session and conversation id
response = None
first_tag_content = None
existing_first_tag_contents = []
if os.path.exists('existing_first_tag_contents.txt'):
    with open('existing_first_tag_contents.txt', 'r') as contents_file:
        existing_first_tag_contents = contents_file.read().splitlines()

while not response or (first_tag_content and first_tag_content in existing_first_tag_contents):
    existing_first_tag_contents = []
    bard = Bard(token=token, session=session, conversation_id="c_39e2910c03c5a74b", timeout=30)
    response = bard.get_answer(input_text)
    response = {k: list(v) if isinstance(v, set) else v for k, v in response.items()}
    content = response['content']
    first_tag_start = content.find('**')
    first_tag_end = content.find('**', first_tag_start + 2)
    first_tag_content = content[first_tag_start + 2:first_tag_end].strip() if first_tag_start != -1 and first_tag_end != -1 else None

    # Store the existing first tag contents in the list
    if os.path.exists('existing_first_tag_contents.txt'):
        with open('existing_first_tag_contents.txt', 'r') as contents_file:
            existing_first_tag_contents = contents_file.read().splitlines()

# Generate a random file name with incremental ID and the current date
random.seed()
current_date = datetime.now().strftime("%Y-%m-%d")

# Read the highest ID from a file or initialize it to 0
highest_id = 0
if os.path.exists('highest_id.txt'):
    with open('highest_id.txt', 'r') as id_file:
        highest_id = int(id_file.read())

# Increment the ID and store it in the file
highest_id += 1
with open('highest_id.txt', 'w') as id_file:
    id_file.write(str(highest_id))

# Add the new first tag content to the list of existing first tag contents
existing_first_tag_contents.append(first_tag_content)

# Filter out None values from existing_first_tag_contents
existing_first_tag_contents = [c for c in existing_first_tag_contents if c is not None]

# Store the updated list of existing first tag contents in the file
with open('existing_first_tag_contents.txt', 'w') as contents_file:
    contents_file.write('\n'.join(existing_first_tag_contents))

# Create the folder based on the current date
folder_name = datetime.now().strftime("%Y-%m-%d")
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# Create the file name using the first tag content
file_name= f"{first_tag_content}.md"

# Define the path to the file inside the articles folder and date folder
file_path = os.path.join("articles", folder_name, file_name)

print(json.dumps(response, indent=2))

# Create the articles folder if it doesn't exist
if not os.path.exists(os.path.join("articles",folder_name)):
    os.makedirs(os.path.join("articles",folder_name))

# Write the content as markdown to the file
with open(file_path, 'w') as file:
    file.write(content)

# Print the response as JSON
# print(json.dumps(response, indent=2))
