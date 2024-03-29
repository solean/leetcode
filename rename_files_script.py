import os
import re
import fileinput

# Rename files in the root directory
for filename in os.listdir('.'):
    if filename.endswith('.py') and re.search(r'\d+\.py$', filename):
        parts = re.split('_(\d+)\.py$', filename)
        if len(parts) == 3:
            new_filename = f'{parts[1]}_{parts[0]}.py'
            print(f'Renaming {filename} to: {new_filename}')
            os.rename(filename, new_filename)

# Update imports in the test files
for filename in os.listdir('./test'):
    if filename.endswith('.py'):
        with fileinput.FileInput(os.path.join('./test', filename), inplace=True, mode='r') as file:
            for line in file:
                # This regex matches 'from name_number import *' patterns
                match = re.match(r'from (\w+)_(\d+) import \*$', line.strip())
                if match:
                    # Reconstruct the import statement with the number first
                    new_import = f'from {match.group(2)}_{match.group(1)} import *'
                    print(new_import)
                else:
                    # If no match, print the line as is
                    print(line, end='')