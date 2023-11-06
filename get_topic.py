# from bardapi import Bard, SESSION_HEADERS
# import os
# import requests
# import json
# import random
# from datetime import datetime

# # Set token
# token = 'YQjiJxS0JS8Wl-R1RDhmOhyItTKCevEdNSr5EWRH4Gh6RL_rBUYzmD9-Kq9ps2zqXpZ9bA.'

# # Set session
# session = requests.Session()
# session.headers = SESSION_HEADERS
# session.cookies.set("__Secure-1PSID", token)

# # Accept user input for the input text
# input_text = "List top 10 trending topic about SME and artificial intelligence in (this.month). Be creative and put the list as javascript object with no variable in format [{id, title, descs}] as utf-8"

# # Give session and conversation id
# bard = Bard(token=token, session=session, conversation_id="c_39e2910c03c5a74b", timeout=30)
# response = bard.get_answer(input_text)

# response = {k: list(v) if isinstance(v, set) else v for k, v in response.items()}

# # Determine the content to write to the file
# if 'code' in response:
#     content = response['code']
# else:
#     content = response['content']

# # Generate a random file name with incremental ID and the current date
# random.seed()
# current_date = datetime.now().strftime("%Y-%m-%d")

# # Read the highest ID from a file or initialize it to 0
# highest_id = 0
# if os.path.exists('highest_id.txt'):
#     with open('highest_id.txt', 'r') as id_file:
#         highest_id = int(id_file.read())

# # Increment the ID and store it in the file
# highest_id += 1
# with open('highest_id.txt', 'w') as id_file:
#     id_file.write(str(highest_id))

# # Create the file name using the incremental ID and current date
# file_name = f"response_{highest_id}_{current_date}.json"

# # Write the content as JSON to the file
# with open(file_name, 'w') as file:
#     json.dump(content, file, indent=2, sort_keys=True, ensure_ascii=False)

# # Print the response as JSON
# print(json.dumps(response, indent=2))



from bardapi import Bard, SESSION_HEADERS
import os
import requests
import json
import random
from datetime import datetime

# Set token
token = 'YQjiJxS0JS8Wl-R1RDhmOhyItTKCevEdNSr5EWRH4Gh6RL_rBUYzmD9-Kq9ps2zqXpZ9bA.'

# Set session
session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token)

# Accept user input for the input text
# input_text = 'List top 7 trending topic about SME and artificial intelligence in (this.month). Be creative and put the list as javascript object with no variable in format [{"id", "title", "descs"}] as utf-8 ensure there is no character after and no whitspace after " ]'
# input_text = 'List top 7 trending topic about SME and artificial intelligence in (this.month). Be creative and put the list inside html tag <p>'
input_text = "I want you to act as a professional blog writer. Write down a story telling type of blog post about SME, artifical intelligence, marketing, branding, route to market, warhouse management, inventory system, recommendation, price analysis, market analysis and all topic related to brands and business use professional tone, make it SEO-friendly, ensure it's not plagiarsm, be creative. Make it engaging and fun to read. use markdown format inside html tag"

# Give session and conversation id
bard = Bard(token=token, session=session, conversation_id="c_39e2910c03c5a74b", timeout=30)
response = bard.get_answer(input_text)

response = {k: list(v) if isinstance(v, set) else v for k, v in response.items()}

# Determine the content to write to the file
# if 'code' in response:
#     content = response['code']
#     if 'null' in content:
#         content = response['content']
# else:
content = response['content']

# Find the index of the opening bracket "["
# start_index = content.find("[")

# Extract the content starting from the opening bracket
# cleaned_content = content[start_index:]

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

# Create the file name using the incremental ID and current date
file_name = f"response_{highest_id}_{current_date}.md"


print(json.dumps(response, indent=2))

# Write the cleaned content as JSON to the file
with open(file_name, 'w') as file:
    file.write(content)

# Print the response as JSON
# print(json.dumps(response, indent=2))
