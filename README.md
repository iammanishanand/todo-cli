# To-Do CLI App

A simple command-line to-do list application built with [Typer](https://typer.tiangolo.com/) in Python.

## Features
- Add tasks 📌
- List tasks 📋
- Mark tasks as completed ✅
- Delete tasks 🗑️

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/iammanishanand/todo-cli.git
   cd todo-cli
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the following command to see available options:
```sh
python todo.py --help
```

### Add a Task
```sh
python todo.py add "Buy groceries"
```

### List Tasks
```sh
python todo.py list
```

### Complete a Task
```sh
python todo.py complete 1
```

### Delete a Task
```sh
python todo.py delete 1
```

## Requirements
See `requirements.txt` for dependencies.

## License
This project is licensed under the MIT License. It is an open-source project built for my portfolio. Feel free to contribute, improve, or use it for your own purposes. Contributions are welcome!

