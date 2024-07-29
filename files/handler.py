# sample_bin_handler.py

# Open the file in binary read mode and read the data
with open('sample.bin', 'rb') as binary_file:
    binary_data = binary_file.read()

# Optionally manipulate the binary data (for demonstration, we'll leave it as is)

# Open a new file in binary write mode and write the binary data
with open('sample_copy.bin', 'wb') as binary_file_copy:
    binary_file_copy.write(binary_data)
