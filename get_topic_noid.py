import os
import requests
import json
import random
from datetime import datetime

import bardapi

# Set token
token = '' #set bard token api

# Define the topics
topics = [
    "SME",
    "small and medium enterprises",
    "entrepreneurship",
    "startups",
    "business development",
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "natural language processing",
    "computer vision",
    "marketing",
    "digital marketing",
    "social media marketing",
    "content marketing",
    "branding",
    "brand identity",
    "brand strategy",
    "brand awareness",
    "route to market",
    "distribution channels",
    "supply chain management",
    "logistics",
    "warehouse management",
    "inventory system",
    "inventory management",
    "stock control",
    "recommendation",
    "personalized recommendations",
    "collaborative filtering",
    "recommender systems",
    "price analysis",
    "pricing strategies",
    "price optimization",
    "competitor analysis",
    "market analysis",
    "market research",
    "customer segmentation",
    "competitive intelligence",
    "brand positioning",
    "customer behavior",
    "market trends",
    "business",
    "business strategy",
    "business planning",
    "financial management",
    "sales and marketing",
    "customer acquisition",
    "customer retention",
    "e-commerce",
    "customer relationship management",
    "CRM",
    "business analytics",
    "data-driven decision making"
]

# Accept user input for the input text
# input_text = "I want you to act as a tech journalist. You will report on breaking news, write feature stories and opinion pieces, develop research techniques for verifying information and uncovering sources, adhere to journalistic ethics, and deliver accurate reporting using your own distinct style, I want the page to be at least 9000 characters long. My first suggestion request is 'I need help writing an article about {} Use markdown format inside HTML tags'".format(random.choice(topics))
input_text = "I want you to act as a professional tech blog writer. Write down a full length blog post about this topic: {} - choose one topic only use professional tone, make it SEO-friendly, ensure it is not plagiarism, be creative. Make it engaging and fun to read. Use markdown format inside HTML tags".format(random.choice(topics))

# Give session and conversation id
response = None
first_tag_content = None
existing_first_tag_contents = []
if os.path.exists('existing_first_tag_contents.txt'):
    with open('existing_first_tag_contents.txt', 'r') as contents_file:
        existing_first_tag_contents = contents_file.read().splitlines()

while not response or (first_tag_content and first_tag_content in existing_first_tag_contents):
    existing_first_tag_contents = []
    response = bardapi.core.Bard(token).get_answer(input_text)
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

# Create the file name using the first tag content
file_name = f"{first_tag_content}.md"

# Define the path to the file inside the articles folder and date folder
file_path = os.path.join("articles", folder_name, file_name)

# Create the articles folder if it doesn't exist
if not os.path.exists(os.path.join("articles", folder_name)):
    os.makedirs(os.path.join("articles", folder_name))

# Write the content as markdown to the file
with open(file_path, 'w') as file:
    file.write(content)

# Print the response as JSON
print(json.dumps(response, indent=2))
