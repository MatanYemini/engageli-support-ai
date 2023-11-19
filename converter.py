import json

# Open the JSON file and read its contents
with open('output.json', 'r') as json_file:
    data = json.load(json_file)

# Open a new file in write mode for the JSONL output
with open('output.jsonl', 'w') as jsonl_file:
    # Write each JSON object as a separate line in the JSONL file
    for item in data:
        json.dump(item, jsonl_file)
        jsonl_file.write('\n')