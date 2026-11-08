# File Objects

# Opening and Closing Files
f = open('test.txt', 'r', encoding='utf-8')

# Modes:
#   r - read
#   w - write
#   a - append
#   r+ - read and write

print(f.name)
print(f.mode)

f.close()  # make sure to close file


# Using context managers - Best Practice
# Reading Files
with open('test.txt', 'r', encoding='utf-8') as f:
    f_contents = f.read()
    print(f_contents)

# Autocamatically cleanups and closes file when context manager ends
print(f.closed)

with open('test.txt', 'r', encoding='utf-8') as f:
    f_contents = f.readline()
    print(f_contents, end='')  # 1st line
    # end='' ignores new line(\n)
    f_contents = f.readline()
    print(f_contents, end='')  # 2nd line

# Use loop to show file data line by line
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

with open('test.txt', 'r', encoding='utf-8') as f:
    size_to_read = 10  # to read first 10 characters from file
    f_contents = f.read(size_to_read)  # 10 characters
    print(f_contents, end='')

    f.seek(0)  # set position e.g. to the beginning position: 0

    f_contents = f.read(size_to_read)  # reads the first 10 characters again
    print(f_contents, end='')

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

# Writing Files
with open('test2.txt', 'w') as f:  # if file exists overwrites else creates that file
    f.write('Test')
    f.seek(0)  # so overwrites from 0 position
    f.write('R')  # result: Rest

# Copying text files
with open('test.txt', 'r', encoding='utf-8') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('python.jpg', 'rb') as rf:  # 'rb' read in bytes
    with open('python_copy.jpg', 'wb') as wf:  # 'wb' write in bytes
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
