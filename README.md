# Json-Data-Extracts:
Install the required libraries:
pip install spacy
python -m spacy download en_core_web_sm
Loads a pre-trained SpaCy model for English language processing (en_core_web_sm).
Retrieves the current working directory and defines the path to a JSON file (hi.json) containing data.
Loads the JSON data from the file.
Iterates over each entry in the JSON data and extracts the response text and corresponding source contexts.
Tokenizes the response and context texts using SpaCy, filtering out stop words and punctuation.
Identifies common content (tokens) between the response and each source context.
If at least 3 common tokens are found, it creates a citation object containing the source ID, context, and link.
Groups the response and its citations into a dictionary-like structure (response_sources).
Writes the extracted citations to a new JSON file (output.json) in the same directory as the input file.
Prints a message indicating the successful creation of the output file.
