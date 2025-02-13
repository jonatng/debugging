# Debugging Project

## Overview
This project is designed to help developers improve their debugging skills by identifying, analyzing, and resolving issues in code. The project contains a series of buggy scripts and debugging tools to practice troubleshooting common programming errors.

## Features
- **Buggy Code Samples**: Various scripts with intentional bugs to practice debugging.
- **Debugging Tools**: Utilization of debugging tools such as gdb, lldb, and built-in debugging functionalities.
- **Logging and Error Handling**: Best practices for logging and handling errors effectively.
- **Testing Framework**: Unit tests to validate fixes and ensure code stability.

## Installation
### Prerequisites
- Python 3.x
- Git
- A text editor or IDE (e.g., VS Code, PyCharm)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/debugging-project.git
   ```
2. Navigate to the project directory:
   ```sh
   cd debugging-project
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### Running the Buggy Scripts
To execute a buggy script, run:
```sh
python buggy_script.py
```

### Debugging the Code
Use debugging tools such as:
- `pdb` (Python Debugger):
  ```sh
  python -m pdb buggy_script.py
  ```
- `print()` statements for simple debugging.
- `logging` module for more structured debugging.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b fix-bug
   ```
3. Commit changes:
   ```sh
   git commit -m "Fixed issue in buggy_script.py"
   ```
4. Push to the branch:
   ```sh
   git push origin fix-bug
   ```
5. Open a Pull Request.

# Running Tests
### Run all tests:
```sh
pytest
```
### Run tests in a specific file:
```sh
pytest tests/test_math_operations.py
```
### Run a specific test function:
```sh
pytest tests/t_test.py::test_add
```
### Run only tests marked as fast:
```sh
pytest -m fast
```
### Run only tests marked as slow:
```sh
pytest -m slow
```
### Show detailed output:
```sh
pytest -v
```
### Stop on first failure:
```sh
pytest -x
```

# Generate a Test Coverage Report
```sh
pip install pytest-cov
pytest --cov=debugging
```

# Run Tests automatically on Code changes
```sh
pip install pytest-watch
pytest-watch
```

## License
This project is licensed under the APACHE License - see the [LICENSE](LICENSE) file for details.

## Contact
For any issues or suggestions, please open an issue on GitHub or contact the maintainer [here](mailto:jonatngu@icloud.com).