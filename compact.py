import json
import os
import re

def remove_comments(json_str):
    # Removes single line comments (//) and block comments (/* */)
    json_str = re.sub(r'//.*?\n|/\*.*?\*/', '', json_str, flags=re.DOTALL)
    return json_str

def compact_json(input_dir, output_dir):
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
                    raw_data = input_file.read()
                    clean_data = remove_comments(raw_data)
                    try:
                        data = json.loads(clean_data)
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from file {input_file_path}")
                        continue
                
                compact_json_str = json.dumps(data, separators=(',', ':'))
                
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(compact_json_str)
                
                print(f"JSON file has been compacted and saved to {output_file_path}")

if __name__ == "__main__":
    input_dir = 'input'
    output_dir = 'output'
    compact_json(input_dir, output_dir)
