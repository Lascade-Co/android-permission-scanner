# Android Project Permission Scanner

This script scans an Android project directory for permissions declared in any XML files and prints the findings directly to the console.

## Requirements
- Python 3.x
- Access to the project directory where the script and Android project reside

## Setup
1. **Clone or download the repository**: Ensure that the `scanner.py` script is located in the root of your Android project.
2. **Python Environment**: You need Python 3.x installed on your system. You can download it from [Python's official site](https://www.python.org/downloads/).

## Usage
1. **Open a terminal** or command prompt.
2. **Navigate to the root of your Android project** where the `scanner.py` script is located.
3. **Run the script** by typing the following command in your terminal:
```python
python scanner.py
```
The script will automatically scan the project directory and subdirectories for any XML files that declare permissions and print the findings to the console.

## Output
The output will list all unique permissions found throughout the XML files in the project. If no permissions are found, it will indicate so.

## Note
- The script assumes all XML files are related to Android configurations. Non-Android XML files might affect the results if they contain similar attributes.
- Ensure that the script has proper read permissions across all directories in the project.