import os
import json

def traverse_directory(root_dir):
    id_counter = 1  # Initialize the ID counter
    results = []  # Initialize the list to store result dictionaries
    
    # Ensure the root_dir is correctly formatted without trailing slash
    root_dir = root_dir.rstrip(os.sep)

    for root, dirs, files in os.walk(root_dir):
        path_parts = root.split(os.sep)
        depth = len(path_parts) - len(root_dir.split(os.sep))

        # Skip the root directory
        if depth < 1:
            continue

        # Determine classification and subclassification based on depth
        if depth == 1:  # Files directly under classification
            classification = path_parts[-1]
            subclassification = None
        elif depth >= 2:  # Files under subclassification
            classification = path_parts[-2]
            subclassification = path_parts[-1]
        else:
            continue  # This should not happen, but added for completeness

        for filename in files:
            file_path = os.path.join(root, filename)

            # Read the file contents
            with open(file_path, 'r', encoding='utf-8') as file:
                contents = file.read()

            # Create the result dictionary, conditionally including subclassification
            result = {
                "id": f"{id_counter:03}",
                "classification": classification,
                "filename": filename,
                "prompt": contents
            }
            if subclassification:
                result["subclassification"] = subclassification

            results.append(result)  # Add the result to the list
            id_counter += 1  # Increment the ID counter

    return results

# Set the directory you want to traverse
samples_dir = './samples'

# Traverse the directory and collect data
data = traverse_directory(samples_dir)

# Optionally, write the results to a JSON file
with open('dataset.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)

