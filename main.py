import os
import ast
import importlib.util
import concurrent.futures

# Function to import module from file
def import_module_from_file(file_path):
    module_name = os.path.splitext(os.path.basename(file_path))[0]  # Extract module name without extension
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Folder containing your Python files
folder_path = r'tests'

# Iterate through files, extract functions, and store in dictionary
function_dict = {}
file_names = [file for file in os.listdir(folder_path) if file.endswith('.py')]

for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    module = import_module_from_file(file_path)
    
    # Extract functions using ast
    for node in ast.walk(ast.parse(open(file_path).read())):
        if isinstance(node, ast.FunctionDef):
            function_dict[node.name] = getattr(module, node.name)

# Execute functions concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=len(file_names)) as executor:
    futures = [executor.submit(function) for function in function_dict.values()]

    # Wait for all tasks to finish
    concurrent.futures.wait(futures)

    # Check the results and print success messages
    for future, test_name in zip(futures, function_dict.keys()):
        try:
            result = future.result()
            assert result is True
            print(f"{test_name} is successful with no errors")
        except AssertionError as e:
            if str(e):
                print(f"{test_name} failed. Error Details: {str(e)}")
            else:
                print(f"{test_name} failed: {result}")
