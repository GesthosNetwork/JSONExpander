import json
import os

def expand_json(input_dir, output_dir):
    if not os.path.isdir(input_dir):
        print(f"The folder {input_dir} was not found.")
        return

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith(".json"):
                input_file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_dir)
                output_sub_dir = os.path.join(output_dir, relative_path)
                
                if not os.path.isdir(output_sub_dir):
                    os.makedirs(output_sub_dir)
                
                output_file_path = os.path.join(output_sub_dir, filename)
                
                with open(input_file_path, 'r', encoding='utf-8') as input_file:
                    data = json.load(input_file)
                
                expanded_json = json.dumps(data, indent=2)  # indent value
                
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(expanded_json)
                
                print(f"JSON file has been expanded and saved to {output_file_path}")

if __name__ == "__main__":
    input_dir = 'input'
    output_dir = 'output'
    expand_json(input_dir, output_dir)
