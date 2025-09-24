import os

def list_directory_contents(path='.'):
    """
    Prints the contents of the directory given by `path`.
    Defaults to current directory if no path provided.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return

    if not entries:
        print(f"No entries found in directory: {path}")
    else:
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)

if __name__ == "__main__":
    # You can change this path to any directory you like
    directory_path = input("Enter the directory path (leave blank for current directory): ").strip()
    if directory_path == "":
        directory_path = '.'
    list_directory_contents(directory_path)
