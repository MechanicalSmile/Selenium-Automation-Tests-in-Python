# Selenium Test Examples in Python

This repository contains example uses of Selenium tests in Python. Before running the tests, make sure to download the ChromeDriver and place it in the main directory.

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
