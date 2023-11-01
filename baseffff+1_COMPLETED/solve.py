import base65536

# Specify the filename
filename = "baseffff1"

# Try to open and read the file
try:
    with open(filename, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    # Decode the file contents using base65536
    decoded_data = base65536.decode(file_contents)

    # Print the decoded data
    #print(decoded_data)

    # Search for the flag{} in the decoded data and extract it
    flag_start = decoded_data.find(b'flag{')
    flag_end = decoded_data.find(b'}', flag_start)

    if flag_start != -1 and flag_end != -1:
        flag_contents = decoded_data[flag_start:flag_end + 1]
        print(flag_contents.decode('utf-8'))

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")