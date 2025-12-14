import sys, os
import readline
import re

SHELL_BUILTIN = ["echo", "exit", "type", "history", "pwd"]
PATH = os.getenv("PATH", "")
paths = PATH.split(":")
HISTORY = []

def find_exec(cmd):
    for path in paths:
        full_path = f"{path}/{cmd}"
        try:
            if os.access(full_path, os.X_OK):
                return full_path
        except FileNotFoundError:
            continue
    return None

def sync_readline_history():
    """Sync readline history with our HISTORY list"""
    readline.clear_history()
    for cmd in HISTORY:
        readline.add_history(cmd)

def format(text: str, top_level:bool=True):
    if '\"' in text:
        final = ""
        arguments = re.split(r'\s+(?=(?:[^"]*"[^"]*")*[^"]*$)', text)
        for arg in arguments:
            if '\"\"' in arg:
                arg = re.sub('\"\"', '', arg)
            if len(arg) >= 2 and arg[0] == arg[-1] == '\"':
                arg = arg[1:-1]
            if len(arguments) == 1:
                return arg
            final += format(arg, top_level=False) + " "
        return final.strip()
    elif "'" in text:
        final = ""
        arguments = re.split(r"\s+(?=(?:[^']*'[^']*')*[^']*$)", text)
        for arg in arguments:
            if "''" in arg:
                arg = re.sub(r"''", '', arg)
            if len(arg) >= 2 and arg[0] == arg[-1] == "'":
                arg = arg[1:-1]
            if len(arguments) == 1:
                return arg
            final += format(arg, top_level=False) + " "
        return final.strip()
    else:
        if top_level:
            return re.sub(r"\s+", " ", text).strip()
        return text
        
def main():
    global HISTORY
    
    sync_readline_history()
    
    try:
        command = input("$ ").strip()
    except EOFError:
        sys.exit()
    HISTORY.append(command)
    
    if command == "exit":
        sys.exit()
    elif command.startswith("echo "):
        text = command[5:]
        print(format(text))
    elif command.startswith("pwd"):
        print(os.getcwd())
    elif command.startswith("cd"):
        try:
            if command[3:]=="~":
                home = os.getenv("USERPROFILE")
                os.chdir(home)
            else:
                os.chdir(command[3:])
        except FileNotFoundError:
            print(f"cd: {command[3:]}: No such file or directory")
    elif command.startswith("history"):
        parts = command.split(" ")
        if len(parts) > 1:
            try:
                count = int(parts[1])
                start = max(0, len(HISTORY) - count)
                for i in range(start, len(HISTORY)):
                    print(f"{i+1} {HISTORY[i]}")
            except ValueError:
                print("history: invalid count")
        else:
            for index, cmd in enumerate(HISTORY):
                print(f"{index+1} {cmd}")
    elif command.startswith("type "):
        cmd_name = command[5:].strip()
        if cmd_name in SHELL_BUILTIN:
            print(f"{cmd_name} is a shell builtin")
        elif find_exec(cmd_name):
            print(f"{cmd_name} is {find_exec(cmd_name)}")
        else:
            print(f"{cmd_name}: not found")
    elif find_exec(command.split(" ")[0]):
        os.system(command)
    else:
        print(f"{command}: command not found")

if __name__ == "__main__":
    try:
        while True:
            main()
    finally:
        histfile = os.path.expanduser("~/.myshell_history")
        readline.write_history_file(histfile)
