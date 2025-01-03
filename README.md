# GitIgnore Large Files

A simple Python script that scans your project folder for files larger than **100 MB** and automatically appends them to your `.gitignore` file. This prevents large files from being accidentally committed in the future.

## Features

-   Recursively scans all files in your project (excluding `.git/`).
-   Automatically generates a `.gitignore` if none exists.
-   Adds any file over 100 MB to `.gitignore`.
-   Optionally warns you if a file is already tracked by Git.

## How It Works

1. **Scans Your Directory**: Walks through the entire project folder.
2. **Checks File Sizes**: Identifies files larger than 100 MB.
3. **Updates `.gitignore`**: Appends large file paths (in a consistent, cross-platform format) so Git will ignore them going forward.

> **Note**: If a file has already been committed to your repository in the past, Git will still track it in your history. You’ll need to remove it or rewrite the Git history if you want it fully removed.

Below is an **example README** section that you can use to guide your users on installing and using your `.ipynb` script. Feel free to adjust the language or formatting to suit your project:

---

## Installation and Usage

1. **Download the Notebook**

    - Download the `.ipynb` file from this repository to your local machine.

2. **Run It**

    - Place the notebook in the **top-level directory** (or wherever you want to manage `.gitignore`).
    - Open the notebook (e.g., in Jupyter, VS Code, Google Colab, etc.) and run all cells.

3. **Automatic Git Ignore**
    - The script will scan for any files larger than **100 MB**.
    - If a `.gitignore` file already exists, the script **appends** a new entry with paths to files exceeding 100 MB.
    - If `.gitignore` does not exist, it creates one for you and includes those large files.

That’s it! You should now have a `.gitignore` set to automatically **ignore** all files over **100 MB** in your repository. Make sure to commit your updated `.gitignore` to keep it in version control.

## Removing Already Committed Large Files

If you have already committed large files before, adding them to `.gitignore` **won’t** remove them from your repository’s history. To remove those files from Git tracking, you may need commands like:

```bash
git rm --cached path/to/largefile
git commit -m "Remove large file from Git tracking"
```

Or, for more thorough removal, you might need to rewrite Git history using tools like [Git filter-repo](https://github.com/newren/git-filter-repo) or [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/).

## Contributing

Feel free to open issues or pull requests if you’d like to suggest improvements or new features.

## License

This project is released under the [MIT License](LICENSE). You’re free to use, modify, and distribute it under the terms of the license.
