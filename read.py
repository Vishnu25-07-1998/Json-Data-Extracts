import os
import json
import spacy
import re

# Load a pre-trained SpaCy model
nlp = spacy.load("en_core_web_sm")

# Get the current working directory
current_directory = os.getcwd()
print("Current directory:", current_directory)

# Define the path to the JSON file
file_path = os.path.join(current_directory, 'hi.json')
print('file_path', file_path)

# Load the JSON data from the file
with open(file_path, 'r') as f:
    data = json.load(f)


# List to store responses and their corresponding source ID and context
response_sources = []

for entry in data["data"]["data"]:
    response = entry["response"]
    response_tokens = set(token.text.lower() for token in nlp(response) if not token.is_stop and not token.is_punct)
    # response_tokens = set(part for token in nlp(response) for part in re.split(r'\W+', token.text.lower()) if not token.is_stop and not token.is_punct if part.strip())
    # print('response: ', response_tokens)
    sources = entry["source"]
    citations = []
    for source in sources:
        context = source["context"]
        context_tokens = set(token.text.lower() for token in nlp(context) if not token.is_stop and not token.is_punct)
        # context_tokens = set(part for token in nlp(context) for part in re.split(r'\W+', token.text.lower()) if not token.is_stop and not token.is_punct and 'www' not in part and 'com' not in part and 'https' not in part and part.strip())
        # print('context: ', context_tokens)
        common_contents = response_tokens.intersection(context_tokens)
        # print(common_contents)
        if len(common_contents) >= 3:
            citation = {
                "id": source["id"],
                "context": context,
                "link": source["link"]
            }
            citations.append(citation)
    response_sources.append({
        "response": response,
        "citations": citations
    })
    

# Define the output file path
output_file_path = os.path.join(current_directory, 'output.json')

# Write the extracted citations to the output JSON file
with open(output_file_path, 'w') as f:
    json.dump(response_sources, f, indent=4)

print("Output JSON file created successfully at:", output_file_path)
