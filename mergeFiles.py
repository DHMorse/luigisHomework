import os
from pathlib import Path

def combine_files(input_directory, output_file):
    """
    Combines all .py and .txt files in the input directory into a single text file,
    with filenames as section headers.
    
    Args:
        input_directory (str): Path to the directory containing the files
        output_file (str): Path to the output file
    """
    # Create a Path object for the input directory
    input_path = Path(input_directory)
    
    # Get all .py and .txt files in the directory
    files = list(input_path.glob('*.py'))
    
    # Sort files to ensure consistent output
    files.sort()
    
    # Create or overwrite the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_path in files:
            try:
                if file_path.name == 'mergeFiles.py':
                    continue
                # Write the file name as a header
                outfile.write(f'\n{"="*50}\n')
                outfile.write(f'File: {file_path.name}\n')
                outfile.write(f'{"="*50}\n\n')
                
                # Read and write the contents of the file
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    
                # Add a newline between files
                outfile.write('\n')
                
            except Exception as e:
                outfile.write(f'Error reading {file_path.name}: {str(e)}\n')
                continue

if __name__ == '__main__':
    # Example usage
    input_dir = './hisCode'  # Current directory
    output_file = './combined_files.txt'
    
    combine_files(input_dir, output_file)
    print(f'Files have been combined into {output_file}')