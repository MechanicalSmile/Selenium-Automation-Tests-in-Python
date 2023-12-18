# Selenium Test Examples in Python

This repository contains example uses of Selenium tests in Python. Before running the tests, make sure to download the ChromeDriver and place it in the main directory.

## ⚠️ Warning: Concurrent Test Execution

This test script executes each test concurrently using a thread pool. The number of worker threads is dynamically set based on the number of tests in the specified folder. Be aware that running a large number of tests concurrently may cause performance issues and overwhelm system resources.

## Setup Instructions

1. **Download ChromeDriver:**
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) to download the appropriate version of ChromeDriver for your system.
   - Ensure that you download a version compatible with your Chrome browser.

2. **Extract the ChromeDriver:**
   - Extract the downloaded ChromeDriver zip file.

3. **Place ChromeDriver in the Main Directory:**
   - Move the extracted ChromeDriver executable to the main directory of this repository.

## Install Python

If you don't have Python installed, you can download it from the official [Python website](https://www.python.org/downloads/). Follow the installation instructions for your operating system.

## Install Dependencies

Create a virtual environment and install the required dependencies using the provided `requirements.txt` file:

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Folder Structure

The folder structure is essential for the script to discover and execute the tests. Ensure that your tests are organized within the specified folder (`tests` in this example).

# Overview of Dynamic Test Execution

In this project, i've implemented a dynamic test execution mechanism that allows you to organize and execute Selenium tests defined in separate Python files. This approach provides flexibility and scalability by automatically discovering and running tests without explicit script modifications.

## How it Works

The main script (`main.py`) utilizes the following concepts and functionalities:

1. **Importing Modules Dynamically:**
   - The `import_module_from_file` function allows us to import Python modules dynamically from specific files. It takes the file path as input, extracts the module name, and imports the module using `importlib`.

2. **Extracting Functions Using AST (Abstract Syntax Trees):**
   - The script iterates through each Python file in the specified folder using `os.listdir` and `os.path.join`.
   - It then uses the `ast` module to parse the Python code and extract function definitions. Functions are stored in a dictionary (`function_dict`), where the keys are function names and the values are the actual function objects.

3. **Concurrent Execution of Functions:**
   - The script utilizes the `concurrent.futures.ThreadPoolExecutor` to execute functions concurrently.
   - It submits each function to the executor, and the results are collected in a list of futures.

4. **Handling Results:**
   - After the concurrent execution, the script checks the results and prints success messages or failure details.
   - If a test function raises an `AssertionError`, it prints the failure details. If an unexpected error occurs, it prints a general failure message.

## How to Use

1. Place your Selenium test scripts (Python files) in the designated folder (specified by `folder_path`).
2. Run the `main.py` script.

Feel free to customize the folder path and script according to your project structure. This dynamic test execution mechanism allows you to easily add or modify test scripts without modifying the main execution script.

## **Running the Selenium Tests** 
After completing the setup and installing Python and the dependencies, you can run the Selenium tests using your preferred test runner or by executing the test scripts directly.
```bash
python main.py
```
Make sure you have Python and the required dependencies installed before running the tests.


## **Deactivating and Deleting the Virtual Environment**
When you're done working on the project, you can deactivate and delete the virtual environment.

### **Deactivate the Virtual Environment**
To deactivate the virtual environment, run the following command:

```bash
deactivate
```

### **Delete the Virtual Environment**
If you want to delete the virtual environment, simply remove the "venv" directory. Use the following command:

```bash
# On Unix-based systems (Linux or macOS)
rm -rf venv

# On Windows
rmdir /s /q venv
```

## **Dependencies**
The dependencies are listed in the requirements.txt file.
Chrome WebDriver: You need to download ChromeDriver separately. Follow the setup instructions in the main section to download and place it in the main directory.

## **Contributing**
If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
