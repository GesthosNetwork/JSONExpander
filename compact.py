import json
import os

def compact_json(input_dir, output_dir):
    if not os.path.isdir(input_dir):
        print(f"The folder {input_dir} was not found.")
        return

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)
            
            with open(input_file_path, 'r') as input_file:
                data = json.load(input_file)
            
            compact_json = json.dumps(data, separators=(',', ':'))
            
            with open(output_file_path, 'w') as output_file:
                output_file.write(compact_json)
            
            print(f"JSON file has been compacted and saved to {output_file_path}")

if __name__ == "__main__":
    input_dir = 'input'
    output_dir = 'output'
    compact_json(input_dir, output_dir)
