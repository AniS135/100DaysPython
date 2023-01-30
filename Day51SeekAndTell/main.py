with open('.\\Day51SeekAndTell\\file.txt', 'r') as f:
    # To Move the pointer to a certain position from starting we use seek function
    # Will move to 10th byte in the file
    f.seek(10)

    # Tells the current position of pointer after seeking
    print(f.tell())

    # Read the next 5 bytes
    
    data = f.read(5)

    print(data)

with open('.\\Day51SeekAndTell\\sample.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5) # It limits the size of bytes in file

with open ('.\\Day51SeekAndTell\\sample.txt', 'r') as f:
    print(f.read())