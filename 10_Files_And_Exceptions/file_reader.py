from pathlib import Path

path = Path(r"D:\CSC\CSC_141\10_Files_And_Exceptions\pi_digits.txt")
contents = path.read_text().rstrip() #read text from file
# contents = contents.rstrip() #remove whitespace from the right side of the string
print(contents) #print content of file


# curr = path.cwd() #current working directory
# print(repr(path.name)) #file name
# print(repr(path.stem)) #file stem
# print(repr(path.suffix)) #file suffix
# #-------------Watching a youtube video on pathlib-------------
# print(repr(path.parent)) #OS path file parent
# print(repr(path)) #OS path file

# Short key for comment is ctrl + /