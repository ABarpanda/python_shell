


https://github.com/user-attachments/assets/d9e50c80-2055-4196-ab2d-847d5a1929d3



# 🐚 PyShell — A Minimal Shell Clone in Python

PyShell is a lightweight, interactive shell clone written in **Python**, designed to mimic the behavior of a basic Unix shell. It implements a set of commonly used shell builtins and supports interactive command navigation and quoting/escaping.

---

## ✨ Features

- **Built-in Commands**
  - `echo` — print text to standard output  
  - `pwd` — display the current working directory  
  - `type` — identify whether a command is a shell builtin  
  - `history` — view previously executed commands  
  - `exit` — exit the shell  

- **Interactive Command Navigation**
  - Navigate through command history using:
    - ⬆️ **Up Arrow** — previous command  
    - ⬇️ **Down Arrow** — next command  

- **Quoting & Escaping Support**
  - Supports **single quotes (`'`)** and **double quotes (`"`)** in `echo`
  - Preserves whitespace and quoted strings similar to a real shell

- **REPL-style Interface**
  - Continuous Read–Eval–Print Loop for an interactive shell experience

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8+**

### Run the Shell

```bash
pip install -r requirements.txt
python main.py
```

---

## 🧪 Example Usage

```bash
$ echo hello world
hello world

$ echo "hello     world"
hello     world

$ echo 'shell''clone'
shellclone

$ pwd
/home/user/projects/pyshell

$ history
1 echo hello world
2 pwd

$ type echo
echo is a shell builtin

$ exit
```

---

## 🛠️ Supported Builtins

| Command   | Description                                    |
| --------- | ---------------------------------------------- |
| `echo`    | Prints arguments to stdout with quote handling |
| `pwd`     | Prints current working directory               |
| `type`    | Identifies builtin commands                    |
| `history` | Displays command history                       |
| `exit`    | Exits the shell                                |

---

## 📂 Project Structure

.
├── main.py        # Main shell loop
└── README.md

## 🎯 Goals of the Project

- Understand how shells parse and execute commands
- Implement interactive terminal features in Python
- Practice handling quoting, escaping, and command history

---

## ⚠️ Limitations

- External command execution is not supported
- Redirection (`>`, `<`) and piping (`|`) are not implemented
- Quoting support is limited to `echo`

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 🙌 Acknowledgements

Inspired by Unix shells like **bash** and **sh**, and built as a learning-focused implementation.

---

Made with ❤️ by Amritanshu
