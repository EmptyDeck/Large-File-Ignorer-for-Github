import os
import sys


def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


def escape_gitignore_entry(path):
    result = ''
    for char in path:
        if char == '[':
            result += '\\['
        elif char == ']':
            result += '\\]'
        else:
            result += char
    if result.startswith('#'):
        result = '\\' + result
    if result.startswith('!'):
        result = '\\' + result
    return result


def main():
    SIZE_THRESHOLD = 100 * 1024 * 1024
    base_dir = os.getcwd()

    gitignore_path = os.path.join(base_dir, '.gitignore')

    existing_entries = set()
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if stripped and not stripped.startswith('#'):
                    existing_entries.add(escape_gitignore_entry(stripped))

    all_files = []
    for root, dirs, files in os.walk(base_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for filename in files:
            fp = os.path.join(root, filename)
            if fp != gitignore_path:
                all_files.append(fp)

    total = len(all_files)
    if total == 0:
        print("No files to scan.")
        return

    new_entries = []
    for i, fp in enumerate(all_files, start=1):
        print_progress_bar(i, total, prefix='Scanning', suffix='Complete', length=40)
        try:
            if os.path.getsize(fp) > SIZE_THRESHOLD:
                rel = os.path.relpath(fp, base_dir).replace('\\', '/')
                escaped = escape_gitignore_entry(rel)
                if escaped not in existing_entries:
                    new_entries.append(escaped)
        except (FileNotFoundError, PermissionError):
            pass
    print()

    if new_entries:
        with open(gitignore_path, 'a', encoding='utf-8') as f:
            f.write('\n# Files over 100 MB (Automatically added)\n')
            for entry in new_entries:
                f.write(entry + '\n')
        print("Added to .gitignore:")
        for entry in new_entries:
            print(f"  {entry}")
    else:
        print("No new large files found.")


if __name__ == '__main__':
    main()
