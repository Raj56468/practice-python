input_file_path = "file IO/numbers.txt"
output_file_path = "file IO/even_numbers.txt"

try:
    # --- Step 1: Read from the input file ---
    with open(input_file_path, "r") as file:
        # Read the single line of text and split it by commas to get individual number strings
        content = file.read()
        number_strings = content.split(',')
        
        # Convert strings to integers and filter for even numbers
        even_numbers = [int(num.strip()) for num in number_strings if num.strip() and int(num.strip()) % 2 == 0]
        
        print(f"Found even numbers: {even_numbers}")
    
    # --- Step 2: Write the even numbers to the output file ---
    with open(output_file_path, "w") as file:
        for number in even_numbers:
            # Write each number followed by a newline character
            file.write(f"{number}\n")
    
    print(f"Successfully wrote even numbers to '{output_file_path}'")
    
except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")