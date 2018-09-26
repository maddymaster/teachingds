try:
    f = open('filefortest', 'r')
    f.write("Putting some text inside this file")
except IOError:
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()