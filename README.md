# GitIgnore Large Files

A Python script that scans for files larger than **100 MB** and automatically add them to your `.gitignore` file. This prevents large files from being accidentally committed in the future.

## Installation and Usage

1. **Download the Python file**

    - Download the `ignore_big_files.py` file from this repository to your local machine.

2. **Run It**

    - Place the py file in the **top-level directory** (or wherever you want to manage `.gitignore`).
    - Rut it

3. **Automatic Git Ignore**
    - The script will scan for any files larger than **100 MB**.
    - If a `.gitignore` file already exists, the script **appends** a new entry with paths to files exceeding 100 MB.
    - If `.gitignore` does not exist, it creates one for you and includes those large files.

That’s it! You should now have a `.gitignore` set to automatically **ignore** all files over **100 MB** in your repository. Make sure to commit your updated `.gitignore` to keep it in version control.
