import os

try:
    os.remove("../3. File Writer/my_first_file.txt")
except FileNotFoundError:
    print("File already deleted!")


# Create a program that deletes the file you created in the previous task.
# If you try to delete the file multiple times, print the message:
#          'File already deleted!'.