import subprocess


def run_file(file_name):
    subprocess.run(["python", file_name])


def main():
    scripts = {
        "1": ("DeleteFile.py", "Delete a file or folder"),
        "2": ("FileCreate.py", "Create a file or folder"),
        "3": ("ReadFolder.py", "Read the contents of a folder"),
        "4": ("GetInfo.py", "Retrieve site information"),
    }

    print("Select an option:")
    for key, (file_name, description) in scripts.items():
        print(f"{key}: {description}")

    selection = input("Enter the number of the script you want to run: ")

    if selection in scripts:
        run_file(scripts[selection][0])
    else:
        print("Invalid selection.")


if __name__ == "__main__":
    main()
