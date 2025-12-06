input_file_path = "file IO/file1.txt"
output_file_path = "file IO/file2.txt"

try:
    with open(input_file_path, "r") as input_file:
        content = input_file.read()

    with open(output_file_path, "w") as output_file:
        output_file.write(content)

    print(f"Successfully copied content from '{input_file_path}' to '{output_file_path}'")

except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")