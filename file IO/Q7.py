file_name = "file IO/numbers.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()
        total_lines = content.count('\n') + 1
        print(f"Total lines in the file: {total_lines}")
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")